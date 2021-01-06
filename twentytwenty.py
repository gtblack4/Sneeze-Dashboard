import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
#with open(os.path.join('C:\\Users\\Gage\\Downloads\\sneezeAnalysis-master\\sneezeAnalysis-master','Sneezes.csv')) as csvFile:
sneezeData2020 = pd.read_csv('sneezes2020.csv')
sneezeData2021 = pd.read_csv('sneezes2021.csv')


def printLine():
	st.write("farts")

#gets the sum of all the values in the sneezes column
def totalCount(sneezedata):
	sneezeSum=sneezedata.sum(axis=0)
	return sneezeSum[1]

def monthComparisonChart():
	print('fart')

def app():
	st.title('Analysis of 2020 Sneezes')
	st.write('Shortcomings')

	if st.button("2020 Analysis"):
		st.write(totalCount(sneezeData2020))
		st.write(totalCount(sneezeData2021))
	 
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
		st.write(totalCount())


	st.write(sneezeData2021)
	print('fart')
