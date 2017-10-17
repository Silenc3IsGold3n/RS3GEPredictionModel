import sqlite3

con = sqlite3.connect("GE_Data.db")
cur = con.cursor()
cur.execute("alter TABLE item_Record_08_11_2017 rename to item_Record_11_10_2017")
#cur.execute("alter TABLE item_Record_10_11_2017 rename to item_Record_11_10_2017")
con.commit()
cur.close()
con.close()