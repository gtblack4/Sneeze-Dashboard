import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
import functions as mf
#imports the csv file
sneezeData2020 = pd.read_csv('sneezes2020.csv')


def monthComparisonChart():
	print('fart')

def app():
	st.title('Analysis of 2020 Sneezes')
	st.write('2020 At a Glance')
	st.write(mf.sneezeLessDays(sneezeData2020))
	if st.button("2020 Analysis"):
		st.write(mf.totalSum(sneezeData2020))
		st.write(mf.sneezeFitCount(sneezeData2020))
		st.write(mf.dailyAverage(sneezeData2020))
		st.write(mf.sneezeFitAverage(sneezeData2020))
		st.write(mf.getDaysElapsed())
		st.write(mf.dayBreakdown(sneezeData2020))
		

	chart_data = pd.DataFrame(
	     np.random.randn(20, 3),
	     columns=['a', 'b', 'c'])

	map_data = pd.DataFrame(
	    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
	    columns=['lat', 'lon'])


	st.write(chart_data)


	if st.button('Say hello'):
		st.write('Why hello there')
		st.line_chart(chart_data)
		printLine()
	else:
		st.map(map_data)
		st.write('Goodbye')

	if st.button('Click this for'):
		st.write(mf.totalCount())


	st.write(sneezeData2020)
	print('fart')
