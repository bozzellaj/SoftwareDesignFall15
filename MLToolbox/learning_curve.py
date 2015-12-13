""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
num_trials = 250
Cval = float(10)		#C value for the Logistic Regression
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

for count, elem in enumerate(train_percentages):		# Loop the training and testing function for each percentage, also averages the accuracies from each trial.
	training = True
	i = 0

	training_percentage = (train_percentages[count]/float(100))

	trial_accuracies = numpy.zeros(num_trials)


	while training:		# Loops until the number of trails has been completed, puts the accuracy from each trial into an array to be averaged. 
		i = i+1
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=training_percentage)
		model = LogisticRegression(C=Cval)
		model.fit(X_train, y_train)
		trialaccuracy = model.score(X_test,y_test)
		trial_accuracies[i-1]=trialaccuracy
		if i == num_trials-1:
			training = False
	test_accuracies[count] = numpy.mean(trial_accuracies)





fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()