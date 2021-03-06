#Takes the array of sneezedata and returns the Sum of the Sneezes
import numpy as np
import pandas as pd
import datetime as datetime
import streamlit as st
import altair as alt
import calendar
dateFormat = "%I:%M %p %m/%d/%Y"

#TODO finish this function to get the number of days elapsed in the year

def dataBreakdown(sneezedata):
	sneezedata['Day of Week'] = pd.to_datetime(sneezedata['Timestamp']).dt.dayofweek
	sneezedata['Day of Year'] = pd.to_datetime(sneezedata['Timestamp']).dt.dayofyear
	sneezedata['Day of Month'] = pd.to_datetime(sneezedata['Timestamp']).dt.day
	sneezedata['Week Number'] = pd.to_datetime(sneezedata['Timestamp']).dt.isocalendar().week
	sneezedata['Month'] = pd.to_datetime(sneezedata['Timestamp']).dt.month
	sneezedata['Year'] = pd.to_datetime(sneezedata['Timestamp']).dt.year
	sneezedata['Cumulative'] = sneezedata['Number of Sneezes'].cumsum(skipna=False)
	sneezedata['Month Cum'] = sneezedata.groupby(['Year','Month'])['Number of Sneezes'].cumsum()


def buildMonthArray(sneezedata):
	monthArray =[0,0,0,0,0,0,0,0,0,0,0,0,0]
	for row in sneezedata.iterrows():
		monthArray[int(row[1]['Month'])] += int(row[1]['Number of Sneezes'])
	return monthArray

def buildDayArray(sneezedata):
	dayArray =[0]*367
	print(dayArray)
	for row in sneezedata.iterrows():
		dayArray[int(row[1]['Day of Year'])] += int(row[1]['Number of Sneezes'])
	return dayArray



def getDaysElapsed():
	today = datetime.date.today()
	print(today)

	return today


def totalSum(sneezedata):
	sneezeSum = sneezedata.sum(axis=0)['Number of Sneezes']
	return sneezeSum

#Takes the array of sneezedata and returns the daily average
def dailyAverage(sneezedata):
	sneezeYear = pd.to_datetime(sneezedata['Timestamp'][0]).year
	thisYear = pd.to_datetime(datetime.date.today()).year
	dayOfYear = pd.to_datetime(datetime.date.today()).dayofyear
	if(sneezeYear == thisYear):
		dailyAverage=int(sneezedata.sum(axis=0)['Number of Sneezes'])/dayOfYear
	else:
		if(calendar.isleap(sneezeYear)):
			dailyAverage=int(sneezedata.sum(axis=0)['Number of Sneezes'])/366
		else:
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
	sneezeYear = pd.to_datetime(sneezedata['Timestamp'][0]).year
	thisYear = pd.to_datetime(datetime.date.today()).year
	dayOfYear = pd.to_datetime(datetime.date.today()).dayofyear
	if(sneezeYear == thisYear):
		numDays = np.unique(pd.DatetimeIndex(sneezedata['Timestamp']).date).size
		numDays = dayOfYear - numDays
	else:
		if(calendar.isleap(sneezeYear)):
			numDays = np.unique(pd.DatetimeIndex(sneezedata['Timestamp']).date).size
			numDays = 366 - numDays
		else:
			numDays = np.unique(pd.DatetimeIndex(sneezedata['Timestamp']).date).size
			numDays = 365 - numDays
	return(numDays)

def dayBreakdown(sneezedata):
	dayBreakdown = alt.Chart(sneezedata).mark_bar().encode(
	x=alt.X('day(Timestamp)'),
	y=alt.Y('Number of Sneezes'),
	color=alt.Color('Year:N')
	).properties(width=350)
	return dayBreakdown


def dayBreakdown2(sneezedata):

	#breakdown = [pd.DatetimeIndex(sneezedata['Timestamp']).dayofweek],[sneezedata['Number of Sneezes']]
	dayofweek =[0,0,0,0,0,0,0]
	for row in sneezedata.iterrows():
		dayofweek[int(pd.to_datetime(row[1]['Timestamp']).dayofweek)] += int(row[1]['Number of Sneezes'])
	dayBreakdown = pd.DataFrame({
		'Day of Week': ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
		'Daily Sum' : [dayofweek[6],dayofweek[0],dayofweek[1],dayofweek[2],dayofweek[3],dayofweek[4],dayofweek[5]]
		})

	dayBreakdown = alt.Chart(dayBreakdown).mark_bar().encode(
	x=alt.X('Day of Week:N', sort=None),
	y=alt.Y('Daily Sum:Q'),
	color=alt.Color('Day of Week',legend = None)
	).properties(width=350)
	return dayBreakdown


def monthBreakdown(sneezedata):
	monthArray =[0,0,0,0,0,0,0,0,0,0,0,0,0]

	for row in sneezedata.iterrows():
		monthArray[int(pd.to_datetime(row[1]['Timestamp']).month)] += int(row[1]['Number of Sneezes'])

	monthBreakdown = pd.DataFrame({
		'Month': ["January","February","March","April","May,","June","July","August","September","October","November","December"],
		'Monthly Sum' : [monthArray[1],monthArray[2],monthArray[3],monthArray[4],monthArray[5],monthArray[6],monthArray[7],monthArray[8],monthArray[9],monthArray[10],monthArray[11],monthArray[12]]
		})


	monthBreakdown = alt.Chart(monthBreakdown).mark_bar().encode(
	y=alt.X('Month:N', sort=None),
	x=alt.Y('Monthly Sum:Q'),
	color=alt.Color('Month',legend=None)
	).properties(width=400)


	return monthBreakdown


def cumSum(sneezedata):
	sneezedata['Cumulative'] = sneezedata['Number of Sneezes'].cumsum()
	return sneezedata


def cumulativeComparison(allSneezeData):
	twenty = 2020
	cumSum = [[allSneezeData[0]['Timestamp']],allSneezeData[0]['Number of Sneezes'],[allSneezeData[1]['Timestamp']],allSneezeData[1]['Number of Sneezes']]
	cumSum[0] = cumSum[0][0]
	cumSum[2] = cumSum[2][0]
	st.write(cumSum[0][0])
	for row in allSneezeData:
		#st.write(pd.DataFrame(row))
		row[twenty] = row['Number of Sneezes'].cumsum()
		twenty += 1
		
