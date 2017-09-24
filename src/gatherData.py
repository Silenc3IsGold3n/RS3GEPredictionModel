import json
import requests
import sqlite3
import time
from Item import *


def run(url,page,total_items,current_items,lockobject,initial):
	if(current_items > total_items):
		print('Somethings wrong, currrent items are greater than total items.')
	if(total_items == current_items and initial == True):
		return
	print(url)
	data = requests.get(url)
	if(data.status_code == 404):
		print('Error 404, check if able to connect to server.')
		return
	if(data.status_code == 200):
		if(len(data.text) == 0):
			print('Request Limit, Waiting five seconds.')
			time.sleep(5)
			return run(url,page,total_items,current_items,lockobject,False)
	data = data.json()
	if (total_items == 0):
		total_items = data['total']
		initial = True
	data = data['items']
	print('Found ' + str(len(data)) + ' items.')
	current_items + len(data)
	#print (str(json.dumps(data,indent = 4)))
	
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	date = time.strftime("%d_%m_%Y")
	cur.execute("create table if not exists item_Record_"+date+" (Id int, Type text ,Name text,Current_trend text,Current_price int, Today_trend text, Today_price text, Members bool)")
	
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
		cur.execute(sqlq,(id,))
		if not cur.fetchone()[0]:
			print('Inserting item id = ' + str(id) +' into database.')
			sql = "INSERT INTO item_Record_"+date+ " VALUES (?,?,?,?,?,?,?,?)"
			lockobject.acquire()
			cur.execute(sql,(item_Record.Id,item_Record.Type,item_Record.Name,item_Record.Current_trend,item_Record.Current_price,item_Record.Today_trend,item_Record.Today_price,item_Record.Members))
			con.commit()
		else:
			print('Record already exists.')
		lockobject.release()
	cur.close()
	con.close()
	if(len(data) == 12):
		newurl = url[:-1] + str(page+1)
		return run (newurl,page+1,total_items,current_items,lockobject,initial)
		