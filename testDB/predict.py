import time
import sqlite3
import pandas as pd
import sklearn
dataframes = []
testDataFrame = []





#will only be predicting the cannonball to start
def start_predict():
        global dataframes
        global testDataFrame
        initial_df = pd.DataFrame(dataframes[0])
        initial_df = initial_df.iloc[0]
        print(initial_df)
        initial_price = initial_df.iloc[4]
        initial_trend = initial_df.iloc[3]
        initial_today_price = initial_df.iloc[6]
        initial_today_trend = initial_df.iloc[5]
        print(initial_price)        
        print(initial_trend)
        print(initial_today_price)        
        print(initial_today_trend)



def get_Data():
        global dataframes
        global testDataFrame
        tables = []
        con = sqlite3.connect("GE_Data.db")
        cur = con.cursor()
        table = cur.execute("select name from sqlite_master where type = 'table'")
       # print('Tables in db: ' + str(tables.fetchall()))
       # print(tables.fetchall())
        for i in table.fetchall():
                tables.append(i[0])
        for i in tables[:-1]:
                print('DFs: ' + str(i))
                q = "select * from " + i + " ORDER BY Id"
                dataframes.append(pd.read_sql(q,con))
        for i in tables[-1:]:
                print('TestDF: ' + str(i))
                q = "select * from " + i + " ORDER BY Id"
                testDataFrame.append(pd.read_sql(q,con))
        cur.close()
        con.close()
       # with pd.option_context('display.max_columns', 1000,'display.max_rows',20,'display.width', 10000):
               # for i in dataframes:
                     #   print('DF')
                     #   print(i)
               # print('TestDF')
               # print(testDataFrame)
               # for i in dataframes:
                        #print(i)

	
get_Data()
start_predict()
