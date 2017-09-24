
import requests
import sqlite3
import pandas as pd

def run():
	con = sqlite3.connect("GE_Data.db")
	cur = con.cursor()
	q = "select * from item_Record"
	data_df = pd.read_sql(q,con)
	with pd.option_context('display.max_columns', 17,'display.max_rows',10000):
		print(data_df)
	cur.close()
	con.close()

