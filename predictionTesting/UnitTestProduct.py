import numpy as np
def predicted(features_array,theta_descent):
	f1 = []
	f2 = []
	for i in features_array:
		f1.append(i[0])
		f2.append(i[1])
	theta_one = []
	theta_two = []
	for i,r in enumerate(f1):
		theta_one.append(np.dot(r,theta_descent[0][i]))
	for i,r in enumerate(f2):
		theta_two.append(np.dot(r,theta_descent[1][i]))
	sum1 = np.zeros(len(theta_one[0]))
	for i in theta_one:
		sum1 = sum1 + i
	sum2 = np.zeros(len(theta_two[0]))
	for i in theta_one:
		sum2 = sum2 + i
	predict = sum1 + sum2
	return predict
	
features_array = [[[1.0,1.0,1.0],[1.0,1.0,1.0]],[[1.0,1.0,1.0],[-1.0,1.0,1.0]]]
theta_descent = [[0.0,0.0],[0.0,0.0]]	

print(predicted(features_array,theta_descent))