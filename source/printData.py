
import requests
import sqlite3
import pandas as pd

def run():
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	sql1 = "Select * from item_Record"
	cur.execute(sql1)
	row = cur.fetchall()
	q = "select * from item_Record"
	data_df = pd.read_sql(q,con)
	#pd.options.display
	with pd.option_context('display.max_columns', 17):
		print(data_df)
	#for i in row:
	#data_df = pd.DataFrame(row)
	#print(data_df)
		#for x in i:
			#print(str(x))
	cur.close()
	con.close()

run()