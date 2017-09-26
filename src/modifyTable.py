import sqlite3

con = sqlite3.connect("GE_Data.db")
cur = con.cursor()
cur.execute("drop TABLE item_Record_25_09_2017")
con.commit()
cur.close()
con.close()