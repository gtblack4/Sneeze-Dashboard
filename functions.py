#Takes the array of sneezedata and returns the Sum of the Sneezes
import numpy as np
import pandas as pd
import datetime as datetime
import streamlit as st
dateFormat = "%I:%M %p %m/%d/%Y"

#TODO finish this function to get the number of days elapsed in the year
def getDaysElapsed():
	today = datetime.date.today()
	print(today)

	return today


def totalSum(sneezedata):
	sneezeSum=sneezedata.sum(axis=0)['Number of Sneezes']
	return sneezeSum

#Takes the array of sneezedata and returns the daily average
def dailyAverage(sneezedata):
	dailyAverage=int(sneezedata.sum(axis=0)['Number of Sneezes'])/365
	return dailyAverage

#Takes the array of sneezedata and returns the number of sneezing events
def sneezeFitCount(sneezedata):
	fitCount=sneezedata['Number of Sneezes'].count()
	return fitCount

#Takes the array of sneezedata and returns the average sneezes per sneezing fit
def sneezeFitAverage(sneezedata):
	fitAverage = totalSum(sneezedata)/sneezeFitCount(sneezedata)
	return fitAverage

#Number of days in the year without sneezes
#TODO Update this so it takes in to account how many days in the year have passed
#TODO ALSO LEAPYEARS
def sneezeLessDays(sneezedata):
	numDays = np.unique(pd.DatetimeIndex(sneezedata['Timestamp']).date).size
	numDays = 365 - numDays
	return(numDays)

def dayBreakdown(sneezedata):

	#breakdown = [pd.DatetimeIndex(sneezedata['Timestamp']).dayofweek],[sneezedata['Number of Sneezes']]
	dayofweek =[0,0,0,0,0,0,0]


	for row in sneezedata.iterrows():
		print(pd.to_datetime(row[1]['Timestamp']).dayofweek)
		dayofweek[int(pd.to_datetime(row[1]['Timestamp']).dayofweek)] += int(row[1]['Number of Sneezes'])
	print(dayofweek)
	dayBreakdown = pd.DataFrame({
		'Day of Week': ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
		'Daily Sum' : [dayofweek[6],dayofweek[0],dayofweek[1],dayofweek[2],dayofweek[3],dayofweek[4],dayofweek[5]]
		})
	# dayBreakdown = pd.DataFrame({
	# 	'Sunday': [dayofweek[6]],
	# 	'Monday': [dayofweek[0]],
	# 	'Tuesday': [dayofweek[1]],
	# 	'Wednesday': [dayofweek[2]],
	# 	'Thursday': [dayofweek[3]],
	# 	'Friday': [dayofweek[4]],
	# 	'Saturday': [dayofweek[6]],
	#   	})

	#st.write(dayBreakdown)

	return dayBreakdown
def mapData(sneezedata):
	return "fuck"

def cumSum(sneezedata):
	sneezedata['Cumulative'] = sneezedata['Number of Sneezes'].cumsum()
	return sneezedata

	#print(pd.DatetimeIndex(sneezedata['Timestamp']))
	
	