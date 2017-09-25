import sqlite3

con = sqlite3.connect("GE_Data_Oldschool.db")
cur = con.cursor()
cur.execute("ALTER TABLE item_Record_24_09_2017 RENAME TO item_Record_23_09_2017")
con.commit()
cur.close()
con.close()