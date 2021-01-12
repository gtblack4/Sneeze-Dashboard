import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
import functions as mf
import altair as alt
import gspread
#with open(os.path.join('C:\\Users\\Gage\\Downloads\\sneezeAnalysis-master\\sneezeAnalysis-master','Sneezes.csv')) as csvFile:
sneezeData2020 = pd.read_csv('sneezes2020.csv',sep=";") #.dropna()
sneezeData2021 = pd.read_csv('sneezes2021.csv',sep=";") #.dropna()


def app():
	st.title('Analysis of 2021 Sneezes')
	st.write('Shortcomings')
	atGlance = st.beta_expander("Show/Hide", expanded=True)
	with atGlance:
		cols = st.beta_columns(2)
		cols[0].write("Total Number of Sneezes:")
		cols[1].write(mf.totalSum(sneezeData2021))
		cols[0].write("Total Number of Sneezing Fits:")
		cols[1].write(mf.sneezeFitCount(sneezeData2021))
		cols[0].write("Daily Average:")
		cols[1].write(mf.dailyAverage(sneezeData2021))
		cols[0].write("Average Number of Sneezes per fit:")
		cols[1].write(mf.sneezeFitAverage(sneezeData2021))
		cols[0].write("Days Without Sneezes:")
		cols[1].write(mf.sneezeLessDays(sneezeData2021))

	timeFrame = st.beta_columns(2)
	timeFrame[0].write(mf.dayBreakdown(sneezeData2021))	
	timeFrame[1].write(mf.monthBreakdown(sneezeData2021))


	
	#mapcode
	mapData = sneezeData2021['GeoCode'].str.split(",",n=1,expand=True).rename(columns={0: 'lat',1: 'lon'})
	mapData['lat'] = mapData['lat'].str[:8].astype(float)
	mapData['lon'] = mapData['lon'].str[:8].astype(float)
	map_data = pd.DataFrame(
	    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
	    columns=['lat', 'lon'])

	st.map(mapData)

	#gets the sum of all the values in the sneezes column


	st.write(sneezeData2021)

