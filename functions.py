#Takes the array of sneezedata and returns the Sum of the Sneezes
import numpy as np
import pandas as pd
import datetime as datetime

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

	breakdown = [pd.DatetimeIndex(sneezedata['Timestamp']).dayofweek],[sneezedata['Number of Sneezes']]
	print('buttpussy')
	for row in sneezedata.iterrows():
		if(pd.to_datetime(row[1]['Timestamp']).dayofweek == 7):
				print(row[1]['Timestamp'])
				print(row[1]['Number of Sneezes'])

	#print(pd.DatetimeIndex(sneezedata['Timestamp']))
	
	return sneezedata['Timestamp']