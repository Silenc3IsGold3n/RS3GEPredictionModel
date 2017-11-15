import time
import sqlite3
import pandas as pd
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

traindataframes = []
testDataFrame = []

#this defines how many items we are looking at
#max = 20
predicted_Item = 0

#def predict_next_day():
	#return 0
	
def denormalize_features(features):
	frames = []
	denormalized_features = []
	trend_feature = []
	for i,r in enumerate(traindataframes):
		price_col = r['Current_price']
		price_col = price_col[predicted_Item:predicted_Item+1].values
		price_col = price_col[0]
		change_col = r['Today_price']
		change_col = change_col[predicted_Item:predicted_Item+1]
		
		today_trend = r['Today_trend']
		today_trend = today_trend[predicted_Item:predicted_Item+1]
		
		#parse data and remove + sign
		for j in change_col:
			if '+' in j:
				t = j.replace('+','')
				change_col = change_col.replace(str(j),t)
		for j in change_col:
			change_col = change_col.replace(str(j),float(j))
		change_col = change_col[predicted_Item]
			
		
		initial_price = price_col - change_col
		closing_price = (features[0][i] + 1) * initial_price
		denormalized_features.append(float(closing_price))	
		
		for j in today_trend:
			if (j == 'neutral'):
				trend_feature.append(float(0))
			elif(j == 'positive'):
				trend_feature.append(float(1))
			elif(j == 'negative'):
				trend_feature.append(float(-1))
		
	features = [denormalized_features, trend_feature]
	features = np.array(features)
	
	return features

def gradient_descent():
	global traindataframes
	global testDataFrame
	prediction_frame = testDataFrame[0]
	prediction_frame = prediction_frame['Current_price']
	prediction_frame = prediction_frame[predicted_Item:predicted_Item+1]
	prediction_frame = prediction_frame[predicted_Item]
	
	#=================================================================================================
	#get features
	#this takes the closing price and the initial price Current_price = initial today price is the change is price 
	#that day. So we take closing minus today change to get initial
	#we then normalize this data
	normalized_features = []
	trend_feature = []
	for i in traindataframes:
		
		price_col = i['Current_price']
		price_col = price_col[predicted_Item:predicted_Item+1].values
		price_col = price_col[0]
		change_col = i['Today_price']
		change_col = change_col[predicted_Item:predicted_Item+1]
		
		today_trend = i['Today_trend']
		today_trend = today_trend[predicted_Item:predicted_Item+1]
		
		#parse data and remove + sign
		for j in change_col:
			if '+' in j:
				t = j.replace('+','')
				change_col = change_col.replace(str(j),t)
		for j in change_col:
			change_col = change_col.replace(str(j),float(j))
		change_col = change_col[predicted_Item]
		#part that gets the initial and closing
		
		initial_price = price_col - change_col
		closing_price = price_col
		normalized = ((closing_price/initial_price)-1)
		normalized_features.append(normalized)
		
		for j in today_trend:
			if (j == 'neutral'):
				trend_feature.append(float(0))
			elif(j == 'positive'):
				trend_feature.append(float(1))
			elif(j == 'negative'):
				trend_feature.append(float(-1))
	#frames.append([normalized_features, trend_feature])
		
	#get features
	features = [normalized_features, trend_feature]
	features_array = np.array(features)
	#===================================================================================================
	
	
	
	
	
	#get values array
	#===================================================================================================
	#same as above we are normalizing the values
	frames = []
	normalized_values = []
	prediction_frame_change = testDataFrame[0]
	prediction_frame_change = prediction_frame_change['Today_price']
	prediction_frame_change = prediction_frame_change[predicted_Item:predicted_Item+1]

	#parse data and remove + sign
	for i in prediction_frame_change:
		if '+' in i:
			t = i.replace('+','')
			prediction_frame_change = prediction_frame_change.replace(str(i),t)
	for i in prediction_frame_change:
		prediction_frame_change = prediction_frame_change.replace(str(i),float(i))
	prediction_frame_change = prediction_frame_change[predicted_Item]
	
	#part that gets the initial and closing
	initial_price = prediction_frame - prediction_frame_change
	closing_price = prediction_frame
	normalized = ((closing_price/initial_price)-1)
	normalized_values.append(normalized)

	#get values
	values_array = np.array(normalized_values)
	
	#===================================================================================================
	
	m = 1
	alpha = 0.00001
	num_iterations = 10
	
	#2 is the number of features
	theta_descent = [0,0]
	cost_history = []
	#actual gradient descent part
	for i in range(num_iterations):
		#hypothesis
		#predicted_value = np.dot(features_array.transpose(), theta_descent)
		
		sum1 = np.sum(features_array[0] * theta_descent[0])
		sum2 = np.sum(features_array[0] * theta_descent[1])
		sum3 = np.sum(features_array[1] * theta_descent[0])
		sum4 = np.sum(features_array[1] * theta_descent[1])
		predicted_value = np.sum(theta_descent) + sum1 + sum2 + sum3 + sum4
		
		#get "corectness"
		sum_of_square_errors = np.square(predicted_value - values_array)
		cost = sum_of_square_errors / (2 * m)
		cost_history.append(cost)
		
		#next theta
		theta_descent[0] = theta_descent[0] - alpha/m * np.sum((predicted_value-values_array) * features_array[0])
		theta_descent[1] = theta_descent[1] - alpha/m * np.sum((predicted_value-values_array) * features_array[1])

		#this causes lag
		if(i % 1000 == 0):
			print('Epoch: ' + str(i/1000) + ' : ' + 'Cost: ' + str(cost_history[i]))
		
		
	#all output and debugging 
	cost_history = pd.Series(cost_history)
	
	sum1 = np.sum(features_array[0] * theta_descent[0])
	sum2 = np.sum(features_array[0] * theta_descent[1])
	sum3 = np.sum(features_array[1] * theta_descent[0])
	sum4 = np.sum(features_array[1] * theta_descent[1])
	predictions = np.sum(theta_descent) + sum1 + sum2 + sum3 + sum4
	#predictions = predicted(features_array, theta_descent)
	print('============================================')
	print('Cost History: ', cost_history)
	print('Theta Descent: ',theta_descent)
	print('Alpha: ', alpha)
	print('Iterations: ',num_iterations)

	data_predictions = (values_array[0] - predictions)**2
	mean = values_array[0]
	sq_mean = np.sum((values_array[0] - mean)**2)
	if(sq_mean == 0):
		sq_mean = sq_mean + 0.0000001
	r = 1 - data_predictions / sq_mean
	print('R: ', r)
	
	#denormalize data
	features = denormalize_features(features)
	print('Value day before: ',features[0][-1:])
	print('Actual Price: ', prediction_frame)
	sum1 = np.sum(features[0] * theta_descent[0])
	sum2 = np.sum(features[0] * theta_descent[1])
	sum3 = np.sum(features[1] * theta_descent[0])
	sum4 = np.sum(features[1] * theta_descent[1])
	#predictions = features[0][-1:] - (np.sum(theta_descent) + sum1 + sum2 + sum3 + sum4)
	print('Predicted price difference percent: ',(1+predictions))
	predictions = (1+predictions) * features[0][-1:]
	#print('Theta Descent sum: ', np.sum(theta_descent))
	#print('Prediction change: ',(np.sum(theta_descent) + sum1 + sum2 + sum3 + sum4))
	print('Predictions: ',predictions)
	print('============================================')
	
	day_before = features
	day_before = day_before[0][-1:]
	
	day_before = day_before.transpose()
	fig, ax = plt.subplots()
	ax.plot(prediction_frame,'o',markersize = 1, color = 'green', label = 'Actual Price')
	ax.plot(predictions,'o',markersize = 1, color = 'blue', label = 'Predicted Price')
	ax.plot(day_before,'o',markersize = 1, color = 'red', label = 'Price Previously')
	plt.legend()
	fig2, ax2 = plt.subplots()
	ax2.plot(cost_history,'o',markersize = 1, color = 'blue')
	plt.show()
	#===================================================================================================
	
	
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
