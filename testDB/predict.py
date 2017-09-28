import time
import sqlite3
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier, GradientBoostingClassifier)
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.pipeline import make_pipeline

traindataframes = []
testDataFrame = []


def predict():
	return



def start_predict():
	global traindataframes
	global testDataFrame
	initial_df = pd.DataFrame(traindataframes[0])
	
	id_col = initial_df['Id']
	price_col = initial_df['Current_price']
	trend_col = initial_df['Current_trend']
	today_price_col = initial_df['Today_price']
	today_trend_col = initial_df['Today_trend']
	print(id_col)
	print(price_col) 
	print(price_trend_col)
	print(today_price_col) 
	print(today_price_col)	



def get_Data():
        global traindataframes
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
               # print('DFs: ' + str(i))
                q = "select * from " + i + " ORDER BY Id"
                traindataframes.append(pd.read_sql(q,con))
        for i in tables[-1:]:
               # print('TestDF: ' + str(i))
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
#predict()
