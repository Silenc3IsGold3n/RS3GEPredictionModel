import time
import sqlite3
import pandas as pd

def run():
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	tables = cur.execute("select name from sqlite_master where type = 'table'")
	print('Tables in db: ' + str(tables.fetchall()))
	print('Todays date: ' + str(time.strftime("%d_%m_%Y")))
	print('Enter requested date in d_mm_yyyy format:',end='')
	date = input()
	q = "select * from item_Record_" + date+ " ORDER BY Id"
	data_df = pd.read_sql(q,con)
	print('Sorted DB.')
	with pd.option_context('display.max_columns', 100,'display.max_rows',10000,'display.width', 10000):
		print(data_df)
	cur.close()
	con.close()
run()
