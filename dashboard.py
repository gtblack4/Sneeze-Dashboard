import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
import functions as mf
import altair as alt
import gspread
import time
import functions as mf
#imports the csv file


def app():
	#Reads the CSV files and builds an array of the data


	sneezeData2020 =pd.read_csv('sneezes2020.csv',sep=";")
	sneezeData2021 =pd.read_csv('sneezes2021.csv',sep=";")
	mf.dataBreakdown(sneezeData2020)
	mf.dataBreakdown(sneezeData2021)
	dataTotal = sneezeData2020.append(sneezeData2021)
	st.title("Gage's Sneezes")
	st.write('Hello! My name is Gage Black and I\' been logging my sneezes since 2020. I noticed that I sneezed more than my friends and coworkers, and I set out to prove it. I\'e create a number of graphs in order to help me understand why I\'m sneezing so much.')
	
	timeFrame = st.beta_columns(2)
	timeFrame[0].write(mf.dayBreakdown(dataTotal))	
	timeFrame[1].write(mf.dayBreakdown2(dataTotal))
	lineCompare = sumLineCompare(dataTotal)

	weekCompare = weeklySneezes(dataTotal)
	heatMapChart(dataTotal)
	yearCompareLines(dataTotal)
	#mf.atAGlance(dataTotal)
	st.write(lineCompare)
	st.write(weekCompare)

#Creates a Line Graph to compare Year to Year Cumulative sneezes
def weeklySneezes(dataTotal):
	selection = alt.selection_multi(fields=['Year'], bind='legend')

	scales = alt.selection_interval(bind='scales')

	base = alt.Chart(dataTotal).encode(
	  x=alt.X('yearmonth(Timestamp):T'),
	  y=alt.Y('Number of Sneezes',bin=True),
	  color='Year:N',
	  tooltip=[
	    alt.Tooltip('(Week Number):T', title='Year'),
        alt.Tooltip('monthdate(Timestamp):T', title='Date'),
        alt.Tooltip('Cumulative:Q', title='Total Sneezes')
    ]
	)


	points = base.mark_circle(color='red').encode(



    opacity=alt.value(0)
    	).add_selection(
	    #highlight,
	    scales
	 

	).properties(
	    
	)
	lines = base.mark_line(color='red').encode(
	#opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    size=alt.condition(~selection, alt.value(1), alt.value(3))
	#size=alt.condition(selection, alt.value(1), alt.value(3))
	).add_selection(selection)

	return points + lines

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


	points = base.mark_circle(color='red').encode(



    opacity=alt.value(0)
    	).add_selection(
	    #highlight,
	    scales
	 

	).properties(
	    
	)
	lines = base.mark_line(color='red').encode(
	#opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    size=alt.condition(~selection, alt.value(1), alt.value(3))
	#size=alt.condition(selection, alt.value(1), alt.value(3))
	).add_selection(selection)

	return points + lines

#MAYBE ONLY DO THIS FOR ONE YEAR


def heatMapChart(dataTotal):
	#dataTotal = sneezeData2020
	#dataTotal['Time'] = pd.to_datetime(dataTotal['Timestamp']).dt.time
	#dataTotal['Date'] = pd.to_datetime(dataTotal['Timestamp']).dt.date


	fartChart = alt.Chart(dataTotal).mark_rect().encode(
    alt.X('hours(Timestamp):O', title='hour of day'),
    alt.Y('month(Timestamp):O', title='date'),
    alt.Color('sum(Number of Sneezes):Q', title='Sneezes',scale=alt.Scale(scheme='yellowgreen')),
        tooltip=[
        alt.Tooltip('hours(Timestamp):T', title='Time'),
        alt.Tooltip('sum(Number of Sneezes):Q', title='Total Sneezes'),
        alt.Tooltip('mean(Number of Sneezes):Q', title='Average')
    ]
	)

	st.write(fartChart)

def yearCompare2(dataTotal):
	
	selector = alt.selection_single(empty='all', fields=['gender'])

	base = alt.Chart(dataTotal).properties(
    width=550,
    height=350
).add_selection(selector)

	yearlyComparison = alt.Chart(dataTotal).mark_bar().encode(
    y=alt.Y('sum(Number of Sneezes):Q',axis=alt.Axis(title=None, labels=True)),
    x=alt.X('year(Timestamp):O',axis=alt.Axis(title=None, labels=False)),
    color='Year:O',
    column=alt.Column('month(Timestamp):O',header=alt.Header(title=None, labelOrient='bottom'))
	).configure_scale(bandPaddingInner=0,
                  bandPaddingOuter=0,
).configure_view(
    stroke='transparent'
).configure_facet(spacing=0)




	st.write(yearlyComparison)


def yearCompareLines(dataTotal):
	print('fart')
	selector = alt.selection_single(fields=['Month'])

	color = alt.condition(selector,
                    alt.Color('yearmonth(Timestamp):T',scale=alt.Scale(scheme='yellowgreen')),
                    alt.value('lightgrey'))
	opacity = alt.condition(selector, alt.value(1.0), alt.value(0))
	base = alt.Chart(dataTotal).properties(
	height = 350)

	legend = base.mark_point().encode(
	y=alt.Y('month(Timestamp):N', axis=alt.Axis(orient='right')),
	color=color
	).add_selection(
	selector)

	monthLine = base.mark_line().encode(
	# 	#x=alt.X('monthday(Timestamp):T'),
	x=alt.X('date(Timestamp)'),
	y=alt.Y('Month Cum'),
	color = color,
	opacity = opacity
		
	).add_selection(selector)
	st.write(monthLine | legend)


def yearCompare(dataTotal):
	st.write(dataTotal)
	#selector = alt.selection_single(empty='all', fields=['Number of Sneezes'])
	selector = alt.selection_single(empty='all',fields=['Month'])
	color = alt.condition(selector,
                      alt.Color('Year:O'),
                      alt.value('lightgrey'))

	base = alt.Chart(dataTotal).properties(
    height=350
	).add_selection(selector)

	hist = base.mark_bar().encode(
    y=alt.Y('sum(Number of Sneezes):Q',axis=alt.Axis(title=None, labels=True)),
    x=alt.X('Year:O',axis=alt.Axis(title=None, labels=False)),
    color=color,
    column=alt.Column('Month:O',header=alt.Header(title=None, labelOrient='bottom'))
	).add_selection(selector)


# .configure_scale(bandPaddingInner=0,
#                   bandPaddingOuter=0,
# 	).configure_view(
# 	    stroke='transparent'
# 	).configure_facet(spacing=0)

	
	monthLine = base.mark_line().encode(
		#x=alt.X('monthday(Timestamp):T'),
		x=alt.X('Day of Month'),
		y=alt.Y('Month Cum'),
		color = color
		
	).add_selection(selector)
	st.write(hist & monthLine)