# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2016-03-23 00:27:51
# @Last Modified by:   dutrasr
# @Last Modified time: 2016-03-31 11:27:36

#########################################################################################
# Titanic: Machine Learning from Disaster
# Predict survival on the Titanic using Excel, Python, R & Random Forests
####
# Challenge description:
# In this challenge, we ask you to complete the analysis of what sorts of people were 
# likely to survive. In particular, we ask you to apply the tools of machine learning 
# to predict which passengers survived the tragedy.
####
# Challenge goals:
# For each passenger in the test set, you must predict whether or not they survived 
# the sinking ( 0 for deceased, 1 for survived ).  Your score is the percentage of 
# passengers you correctly predict.
###
#Characteristics to consider:
# Gender: Because women have preference in life boats, they were more susceptible to 
# survive than a man.
# Age: Children and elderly had preference as women.
# Passanger class: People in a higher class cabin was more likely to survive.
# Passanger with children: Passangers with babe and or children in arms could probably
# accompany them. (Not in the documentation, CHECK THIS IPOTESI, use the parch,number 
# of parents/children aboard).
# Sisbp and parch: Passengers with a higher number of parents and kids could have a lower
# chance to survive due the dificult to unit all of them in the middle of caos of the 
# ship sinking.
# Fare: higher passanger fare indicates a higher class passanger.
#########################################################################################

import csv as csv
import numpy as np

import gender as g
import age as a


#####
# Function that load de csv file and returns the total number of people aboard the
# Titanic, how much of them are men and women and two arrays with all the women and
# men data respectively.
def loadFile(data):
	"""
	Function that load de csv file and returns the total number of people aboard the
	Titanic, how much of them are men and women and two arrays with all the women and
	men data respectively.
	"""
	# Accounts the total number of passengers aboard the Titanic
	passengersAboard = np.size(data[0::,1].astype(np.float))

	###
	# Sort all the data in two groups, women stats and men stats for easily mani-
	# pulation later.
	womenStats = data[0::,4] == "female"
	menStats = data[0::,4] != "female"

	womenAboard = data[womenStats,1].astype(np.float)
	menAboard = data[menStats,1].astype(np.float)
	##

	print ('Passengers aboard the Titanic: %.f' %passengersAboard)
	print ('\t - Number of womens aboard: %.f' %np.size(womenAboard))
	print ('\t - Number of mens aboard: %.f' %np.size(menAboard))

	return passengersAboard, womenAboard, menAboard, womenStats, menStats
###

#####

# Main function
def __main__():

	csvData = csv.reader(open('train.csv', 'r'))			# Load the csv file
	header = csvData.__next__()								# Ignores the first line of the file, the header
	data = []												# Variable to hold the file data

	###
	# Skip throuth the csv file adding each row to the data variable and, at the 
	# end, convert the data variable from a list to an array.
	for row in csvData:
		data.append(row[0:])

	data = np.array(data)
	##

	passengerAboard, womenAboard, menAboard, womenStats, menStats = loadFile(data)			# Aquires the basic data to analise the train.csv file
	
###
__main__()