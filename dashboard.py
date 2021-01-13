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
#imports the csv file


def app():
	sneezeData2020 =pd.read_csv('sneezes2020.csv',sep=";")
	sneezeData2021 =pd.read_csv('sneezes2021.csv',sep=";")
	mf.dataBreakdown(sneezeData2020)
	mf.dataBreakdown(sneezeData2021)

	dataTotal = sneezeData2020.append(sneezeData2021)
	st.write(dataTotal)
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


	fartChart = alt.Chart(dataTotal).mark_rect().encode(
    alt.X('hours(Timestamp):O', title='hour of day'),
    alt.Y('month(Timestamp):O', title='date'),
    alt.Color('sum(Number of Sneezes):Q', title='Sneezes'),
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
def yearCompare(dataTotal):
	st.write(dataTotal)
	selector = alt.selection_single(empty='all', fields=['Month Cum'])

	base = alt.Chart(dataTotal).properties(
   
    height=350
	).add_selection(selector)

	hist = base.mark_bar().encode(
    y=alt.Y('sum(Number of Sneezes):Q',axis=alt.Axis(title=None, labels=True)),
    x=alt.X('year(Timestamp):O',axis=alt.Axis(title=None, labels=False)),
    color='Year:O',
    column=alt.Column('month(Timestamp):O',header=alt.Header(title=None, labelOrient='bottom'))
	)


# .configure_scale(bandPaddingInner=0,
#                   bandPaddingOuter=0,
# 	).configure_view(
# 	    stroke='transparent'
# 	).configure_facet(spacing=0)


	monthLine = base.mark_line().encode(
		x=alt.X('monthday(Timestamp):T'),
		y=alt.Y('Month Cum')
		).transform_filter(
    selector
)
	st.write(hist & monthLine)