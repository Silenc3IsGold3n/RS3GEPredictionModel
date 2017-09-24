import time
import sqlite3
import pandas as pd

def run():
	print('Todays date: ' + str(time.strftime("%d_%m_%Y")))
	print('Enter requested date in d_mm_yyyy format:',end='')
	date = input()
	con = sqlite3.connect("GE_Data_Oldschool.db")
	cur = con.cursor()
	q = "select * from item_Record_" + date
	data_df = pd.read_sql(q,con)
	with pd.option_context('display.max_columns', 17,'display.max_rows',10000):
		print(data_df)
	cur.close()
	con.close()

