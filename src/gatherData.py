import json
import requests
import sqlite3
import time
from Item import *
urls = []
current_items_in_cat = 0

def load_urls():
	global urls
	file = open('pageswithnoitems','r')
	urls = file.read().splitlines()		
	file.close()

def reset_current_items():
	global current_items_in_cat
	current_items_in_cat = 0
def get_current_items():
	global current_items_in_cat
	print('current items: ' + str(current_items_in_cat))
	return current_items_in_cat

def get_items_in_category(url):
	items = requests.get(url)
	if(items.status_code == 404):
		print('Error 404, check if able to connect to server.')
		return 0
	if(items.status_code == 200):
		if(len(items.text) == 0):
			print('Request Limit, Waiting five seconds.')
			time.sleep(5)
			return get_items_in_category(url)
	try:
		items = items.json()
	except:
		return get_items_in_category(url)
	x = int(items['total'])
	return x	
	
def run(url,page,lockobject):
	global urls
	global current_items_in_cat
	print(url)
	for u in urls:
		if(u == url):
			print('Url has no items, skipping.')
			return
	
	data = requests.get(url)
	if(data.status_code == 404):
		print('Error 404, check if able to connect to server.')
		return
	if(data.status_code == 200):
		if(len(data.text) == 0):
			print('Request Limit, Waiting five seconds.')
			time.sleep(5)
			return run(url,page,lockobject)
	try:
		data = data.json()
	except:
		return run(url,page,lockobject)
	data = data['items']
	print('Found ' + str(len(data)) + ' items.')
	if(int(len(data)) == 0):
		file = open ('pageswithnoitems','a+')
		file.write(url)
		file.write('\n')
		print('Added ' + url + ' to page filter file.')
		file.close()
		return
	current_items_in_cat = current_items_in_cat + int(len(data))
	#print (str(json.dumps(data,indent = 4)))
	
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	date = time.strftime("%d_%m_%Y")
	cur.execute("create table if not exists item_Record_"+date+" (Id int, Type text ,Name text,Current_trend text,Current_price int, Today_trend text, Today_price text, Members bool)")
	#cur.execute("create table if not exists item_Record_08_11_2017 (Id int, Type text ,Name text,Current_trend text,Current_price int, Today_trend text, Today_price text, Members bool)")
	for i in data:	
		#icon = data['icon']
		#icon_large = data['icon_large']
		id = int(i['id'])
		type  = i['type']
		name = i['name']
		members = i['members']
		current_trend = i['current']['trend']
		current_price = i['current']['price']
		today_trend = i['today']['trend']
		today_price = i['today']['price']		
		item_Record = Item(id,type, name, current_trend,current_price,today_trend,today_price,members)
		
		#Check if item is already in database then 
		sqlq = "SELECT COUNT(1) FROM item_Record_" +date+ " WHERE Id = ?"
		#sqlq = "SELECT COUNT(1) FROM item_Record_08_11_2017 WHERE Id = ?"
		cur.execute(sqlq,(id,))
		if not cur.fetchone()[0]:
			print('Inserting item id = ' + str(id) +' into database.')
			sql = "INSERT INTO item_Record_"+date+ " VALUES (?,?,?,?,?,?,?,?)"
			#sql = "INSERT INTO item_Record_08_11_2017 VALUES (?,?,?,?,?,?,?,?)"
			#lockobject.acquire()
			cur.execute(sql,(item_Record.Id,item_Record.Type,item_Record.Name,item_Record.Current_trend,item_Record.Current_price,item_Record.Today_trend,item_Record.Today_price,item_Record.Members))
			con.commit()
		else:
			print('Record already exists.')
		#lockobject.release()
	cur.close()
	con.close()
	if(len(data) == 12):
		newurl = url[:-1] + str(page+1)
		return run (newurl,page+1,lockobject)
		