import sqlite3

con = sqlite3.connect("GE_Data_Oldschool.db")
cur = con.cursor()
#cur.execute("drop TABLE item_Record_25_09_2017")
cur.execute("alter TABLE item_Record_08_11_2017 rename to item_Record_11_10_2017")
con.commit()
cur.close()
con.close()