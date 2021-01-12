import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
import functions as mf
import altair as alt
import gspread
#imports the csv file


def app():
	sneezeData2020 =pd.read_csv('sneezes2020.csv',sep=";")
	sneezeData2021 =pd.read_csv('sneezes2021.csv',sep=";")
	mf.dataBreakdown(sneezeData2020)
	mf.dataBreakdown(sneezeData2021)
	allSneezeData = [sneezeData2020,sneezeData2021]	
	Timestamp = sneezeData2020['Timestamp'].append(sneezeData2021['Timestamp'])
	sneezeData2020['Year'] = 2020
	sneezeData2021['Year'] = 2021
	dataTotal = sneezeData2020.append(sneezeData2021)

	st.title('Live Dashboard')
	#mf.cumulativeComparison(allSneezeData)
	sumLineCompare(dataTotal)
	heatMapChart(dataTotal)
	yearCompare(dataTotal)




def sumLineCompare(dataTotal):
	selection = alt.selection_multi(fields=['Year'], bind='legend')

	scales = alt.selection_interval(bind='scales')

	base = alt.Chart(dataTotal).encode(
	  x=alt.X('monthdate(Timestamp):T'),
	  y=alt.Y('Cumulative:Q'),
	  color='Year:N',
	  tooltip=[
	    alt.Tooltip('year(Timestamp):T', title='Year'),
        alt.Tooltip('monthdate(Timestamp):T', title='Date'),
        alt.Tooltip('Cumulative:Q', title='Total Sneezes')
    ]
	)


	points = base.mark_circle().encode(
    opacity=alt.value(0)
	).add_selection(
	    #highlight,
	    scales
	 

	).properties(
	    width=600
	)
	lines = base.mark_line().encode(
	#opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    size=alt.condition(~selection, alt.value(1), alt.value(3))
	#size=alt.condition(selection, alt.value(1), alt.value(3))
	).add_selection(selection)

	st.write(points + lines)

#MAYBE ONLY DO THIS FOR ONE YEAR


def heatMapChart(dataTotal):
	#dataTotal = sneezeData2020
	#dataTotal['Time'] = pd.to_datetime(dataTotal['Timestamp']).dt.time
	#dataTotal['Date'] = pd.to_datetime(dataTotal['Timestamp']).dt.date

	monthArray =[0,0,0,0,0,0,0,0,0,0,0,0,0]
	for row in dataTotal.iterrows():
		monthArray[int(pd.to_datetime(row[1]['Timestamp']).month)] += int(row[1]['Number of Sneezes'])

	# lineChartDF = pd.DataFrame({
	# 	'Time': dataTotal['Time'],
	# 	'Date': dataTotal['Date'],
	# 	'Timestamp': dataTotal['Timestamp'],
	# 	'Sneezes': dataTotal['Number of Sneezes']
	# 	})
	fartChart = alt.Chart(dataTotal).mark_rect().encode(
    alt.X('hours(Timestamp):O', title='hour of day'),
    alt.Y('month(Timestamp):O', title='date'),
    alt.Color('sum(Number of Sneezes):Q', title='Sneezes'),
        tooltip=[
        alt.Tooltip('hours(Timestamp):T', title='Time'),
        alt.Tooltip('sum(Sneezes):Q', title='Total Sneezes'),
        alt.Tooltip('median(Sneezes):Q', title='Average')
    ]
	)

	st.write(fartChart)

def yearCompare(dataTotal):
	timeFrames = ['Weeks', 'Months']
	timeFrameDropdown = alt.binding_select(options=timeFrames)
	timeFrameSelect = alt.selection_single(fields=['Timestamp'], bind=timeFrameDropdown, name="Timestamp")
	


	yearlyComparison = alt.Chart(dataTotal).mark_bar().encode(
    x=alt.X('count(Sneezes):Q'),
    y='year(Timestamp):O',
    color='Year:O',
    row='month(Timestamp):O'
	)

	st.write(yearlyComparison)