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


def predict():
	return



def cost():
	cost = 0
	return cost
	
	
def gradient_descent():
	global traindataframes
	global testDataFrame
	prediction_frame = testDataFrame[0]
	prediction_frame = prediction_frame['Current_price']
	
	initial_df = traindataframes[0]
	
	price_col = initial_df['Current_price']
	
	


	
	'''
	#remove +signs
	for i in value_today:
		if '+' in i:
			temp = i.replace('+','')
			value_today = value_today.replace(str(i),temp)
	#convert to floats
	for i in value_today:
		value_today = value_today.replace(str(i),float(i))
	'''
	frames = []
	for i in traindataframes:
		temp = i['Current_price']
		frames.append(temp[0:50])
		
	'''	#remove +signs
	for i in frames:
		for j in i:
			if '+' in j:
				temp = j.replace('+','')
				j = j.replace(str(i),temp)	
	#convert to floats
	for i in frames:
		for j in i:
			j = j.replace(str(j),float(j))
			'''
	#print(frames)
	data_df = pd.concat(frames,axis=1)
	data_df.columns = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
	print(data_df)
	
	#get features
	features = data_df
	features = (features - features.mean())/features.std()
	features_array = np.array(features)
	
	#values_array = np.random.random_sample(50)
	values_array = prediction_frame[0:50]
	values_array = (values_array - values_array.mean())/values_array.std()
	values_array = np.array(values_array)
	m = len(values_array)
	alpha = 0.01
	num_iterations = 100
	
	theta_descent = np.zeros(len(features.columns))
	
	'''theta_descent = [ 0.04983402,  0.04984066,  0.04997515,  0.0499784,   0.0002391,   0.04998249,
	0.04996475,  0.05001895,  0.05001934 , 0.04997175,  0.04997307,  0.04997442,
	0.04998315, 0.05007499,  0.05008444,  0.05008444,  0.05002506,  0.05002304,
	0.05002437,  0.05002436,  0.05018056]
	'''
	cost_history = []

	for i in range(num_iterations):
		#print('Iteration: ' + str(i))
		predicted_value = np.dot(features_array, theta_descent)
		theta_descent = theta_descent + alpha/m * np.dot(values_array - predicted_value, features_array)
		sum_of_square_errors = np.square(np.dot(features_array, theta_descent) - values_array).sum()
		cost = sum_of_square_errors / (2 * m)
		cost_history.append(cost)

	cost_history = pd.Series(cost_history)
	predictions = np.dot(features_array, theta_descent).transpose()
	print('============================================')
	print('Cost History: ', cost_history)
	print('Predictions: ',predictions)
	print('Theta Descent: ',theta_descent)
	print('Alpha: ', alpha)
	print('Iterations: ',num_iterations)
	
	data_predictions = np.sum((values_array - predictions)**2)
	mean = np.mean(values_array)
	sq_mean = np.sum((values_array - mean)**2)
	r = 1 - data_predictions / sq_mean
	print('R: ', r)
	print()
	print('============================================')
	
	df = frames[-1:]
	plot_prediction = np.add(df[0],predictions)
	fig, ax = plt.subplots()
	ax.plot(prediction_frame[0:50],'o',markersize = 1, color = 'green')
	ax.plot(plot_prediction,'o',markersize = 1, color = 'blue')
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
