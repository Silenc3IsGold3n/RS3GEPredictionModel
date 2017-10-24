import time
import sqlite3
import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

'''
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier, GradientBoostingClassifier)
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.pipeline import make_pipeline
'''
traindataframes = []
testDataFrame = []

#def predict_next_day():
	#return 0

def gradient_descent():
	global traindataframes
	global testDataFrame
	prediction_frame = testDataFrame[0]
	prediction_frame = prediction_frame['Current_price']
	prediction_frame = prediction_frame[0:50]
	#prediction_frame = (prediction_frame - prediction_frame.mean())/prediction_frame.std()
	#prediction_frame = np.array(prediction_frame)
	
	frames = []
	for i in traindataframes:
		temp = i['Current_price']
		frames.append(temp[0:50])
		'''
	frames = []
	for i in traindataframes:
		temp = i['Today_price']
		for i in temp:
			if '+' in i:
				t = i.replace('+','')
				temp = temp.replace(str(i),t)
		for i in temp:
			temp = temp.replace(str(i),float(i))
		frames.append(temp[0:50])
		'''
	#print(frames)
	data_df = pd.concat(frames,axis=1)
	data_df.columns = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
	
	
	#get features
	features = data_df
	features = (features - features.mean())/features.std()
	features_array = np.array(features)
	
	
	#values_array = np.random.random_sample(50)
	values = prediction_frame
	values = (values - values.mean())/values.std()
	values_array = np.array(values)
	
	m = len(values_array)
	alpha = 0.01
	num_iterations = 100
	
	theta_descent = np.zeros(len(features.columns))
	
	cost_history = []

	for i in range(num_iterations):
		predicted_value = np.dot(features_array, theta_descent)
		theta_descent = theta_descent + alpha/m * np.dot(values_array - predicted_value, features_array)
		sum_of_square_errors = np.square(np.dot(features_array, theta_descent) - values_array).sum()
		cost = sum_of_square_errors / (2 * m)
		cost_history.append(cost)

		
	#all output and debugging 
	cost_history = pd.Series(cost_history)
	
	predictions = np.dot(features, theta_descent).transpose()
	print('============================================')
	print('Cost History: ', cost_history)
	print('Theta Descent: ',theta_descent)
	print('Alpha: ', alpha)
	print('Iterations: ',num_iterations)
	
	data_predictions = np.sum((values_array - predictions)**2)
	mean = np.mean(values_array)
	sq_mean = np.sum((values_array - mean)**2)
	r = 1 - data_predictions / sq_mean
	print('R: ', r)
	

	
	#denormalize data
	features = ((features * data_df.std()) + data_df.mean())
	print(features)
	predictions = np.dot(features, theta_descent).transpose()
	print('Predictions: ',predictions)
	print('============================================')

	fig, ax = plt.subplots()
	ax.plot(prediction_frame,'o',markersize = 1, color = 'green', label = 'Actual Price')
	ax.plot(predictions,'o',markersize = 1, color = 'blue', label = 'Predicted Price')
	#ax.plot(features,'o',markersize = 1, color = 'red', label = 'Price Previously')
	fig2, ax2 = plt.subplots()
	ax2.plot(cost_history,'o',markersize = 1, color = 'blue')
	plt.show()
	
def get_Data():
        global traindataframes
        global testDataFrame
        tables = []
        con = sqlite3.connect("GE_Data.db")
        cur = con.cursor()
        table = cur.execute("select name from sqlite_master where type = 'table'")
      
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
	
get_Data()
gradient_descent()
#predict()
