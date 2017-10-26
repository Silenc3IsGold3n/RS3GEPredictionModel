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
def denormalize_features(features):
	frames = []
	for i,r in enumerate(traindataframes):
		denormalized_features = []
		price_col = r['Current_price']
		price_col = price_col[0:50]
		change_col = r['Today_price']
		change_col = change_col[0:50]
		
		#parse data and remove + sign
		for j in change_col:
			if '+' in j:
				t = j.replace('+','')
				change_col = change_col.replace(str(j),t)
		for j in change_col:
			change_col = change_col.replace(str(j),float(j))
			
		for j,element in enumerate(price_col): 
			initial_price = element - change_col[j]
			#closing_price = element 
			#normalized = ((closing_price/initial_price)-1)
			closing_price = (features[i][j] + 1) * initial_price
			denormalized_features.append(closing_price)	
		frames.append(denormalized_features)
		
	features = pd.DataFrame(frames).transpose()
	
	return features
	
def gradient_descent():
	global traindataframes
	global testDataFrame
	prediction_frame = testDataFrame[0]
	prediction_frame = prediction_frame['Current_price']
	prediction_frame = prediction_frame[0:50]
	
	#this takes the closing price and the initial price Current_price = initial today price is the change is price 
	#that day. So we take closing minus today change to get initial
	#we then normalize this data
	frames = []
	for i in traindataframes:
		normalized_features = []
		price_col = i['Current_price']
		price_col = price_col[0:50]
		change_col = i['Today_price']
		change_col = change_col[0:50]
		
		#parse data and remove + sign
		for j in change_col:
			if '+' in j:
				t = j.replace('+','')
				change_col = change_col.replace(str(j),t)
		for j in change_col:
			change_col = change_col.replace(str(j),float(j))
		#part that gets the initial and closing
		for j,element in enumerate(price_col):
			initial_price = element - change_col[j]
			closing_price = element 
			normalized = ((closing_price/initial_price)-1)
			normalized_features.append(normalized)	
		frames.append(normalized_features)
		
	#get features	
	features = pd.DataFrame(frames).transpose()
	features_array = np.array(features)
	
	#same as above we ar normalizing the values
	frames = []
	normalized_features = []
	
	prediction_frame_change = testDataFrame[0]
	prediction_frame_change = prediction_frame_change['Today_price']
	prediction_frame_change = prediction_frame_change[0:50]
	
	#parse data and remove + sign
	for i in prediction_frame_change:
		if '+' in i:
			t = i.replace('+','')
			prediction_frame_change = prediction_frame_change.replace(str(i),t)
	for i in prediction_frame_change:
		prediction_frame_change = prediction_frame_change.replace(str(i),float(i))
	#part that gets the initial and closing
	for i,element in enumerate(prediction_frame):
		initial_price = element - prediction_frame_change[i]
		closing_price = element 
		normalized = ((closing_price/initial_price)-1)
		'''
		print('closing_price: ' + str(closing_price))
		#print('todays_change: ' + str())
		print('normalized_price: ' + str(normalized))
		denormalized = (normalized + 1) * initial_price
		print('denormalized_price: ' + str(denormalized))
		'''
		normalized_features.append(normalized)
	for i in normalized_features:
		frames.append(i)
	
	#get values
	values_array = np.array(frames)
	
	
	m = len(values_array)
	alpha = 0.01
	num_iterations = 1000000
	
	theta_descent = np.zeros(len(features.columns))
	cost_history = []
	
	#actual gradient descent part
	for i in range(num_iterations):
		predicted_value = np.dot(features_array, theta_descent)
		theta_descent = theta_descent + alpha/m * np.dot(values_array - predicted_value, features_array)
		sum_of_square_errors = np.square(np.dot(features_array, theta_descent) - values_array).sum()
		cost = sum_of_square_errors / (2 * m)
		cost_history.append(cost)
		print('Iteration: ' + str(i) + ' : ' + 'Cost: ' + str(cost_history[i]))
		
	#all output and debugging 
	cost_history = pd.Series(cost_history)
	
	predictions = np.dot(features_array, theta_descent).transpose()
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
	features = denormalize_features(features)
	predictions = np.dot(features, theta_descent).transpose()
	print('Predictions: ',predictions)
	print('============================================')
	
	day_before = features.transpose()
	day_before = day_before[-1:]
	day_before = day_before.transpose()
	fig, ax = plt.subplots()
	ax.plot(prediction_frame,'o',markersize = 1, color = 'green', label = 'Actual Price')
	ax.plot(predictions,'o',markersize = 1, color = 'blue', label = 'Predicted Price')
	ax.plot(day_before,'o',markersize = 1, color = 'red', label = 'Price Previously')
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
