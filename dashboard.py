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

	st.title('Live Dashboard')
	#mf.cumulativeComparison(allSneezeData)

	dateRange = pd.date_range('2020-01-01','2020-12-31',freq='bm')


	Timestamp = sneezeData2020['Timestamp'].append(sneezeData2021['Timestamp'])
	data2020 = pd.DataFrame(sneezeData2020['Cumulative'])
	data2021 = pd.DataFrame(sneezeData2021['Cumulative'])
	data2020['Year'] = 2020
	data2021['Year'] = 2021
	dataTotal = data2020.append(data2021)




	lineChartDF = pd.DataFrame({
		'Timestamp': Timestamp,
		'Cumulative': dataTotal['Cumulative'],
		'Year': dataTotal['Year']
		})

	highlight = alt.selection(type='single', on='mouseover',
        fields=['Year'], nearest=True)


	base = alt.Chart(lineChartDF).encode(
	  x=alt.X('monthdate(Timestamp):T'),
	  y=alt.Y('Cumulative:Q'),
	  color='Year:N'
	)

	points = base.mark_circle().encode(
    opacity=alt.value(0)
	).add_selection(
	    highlight
	).properties(
	    width=600
	)
	lines = base.mark_line().encode(
    size=alt.condition(~highlight, alt.value(1), alt.value(3))
	)

	st.write(points + lines)