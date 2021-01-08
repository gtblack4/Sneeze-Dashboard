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
sneezeData2020 = pd.read_csv('sneezes2020.csv',sep=";") #.dropna()


def monthComparisonChart():
	print('fart')

def app():
	
	st.title('Analysis of 2020 Sneezes')
	st.write('2020 At a Glance')

	atGlance = st.beta_expander("Show/Hide", expanded=True)
	with atGlance:
		cols = st.beta_columns(2)
		cols[0].write("Total Number of Sneezes:")
		cols[1].write(mf.totalSum(sneezeData2020))
		cols[0].write("Total Number of Sneezing Fits:")
		cols[1].write(mf.sneezeFitCount(sneezeData2020))
		cols[0].write("Daily Average:")
		cols[1].write(mf.dailyAverage(sneezeData2020))
		cols[0].write("Average Number of Sneezes per fit:")
		cols[1].write(mf.sneezeFitAverage(sneezeData2020))
		cols[0].write("Days Withou Sneezes:")
		cols[1].write(mf.sneezeLessDays(sneezeData2020))



	
	

	map_data = pd.DataFrame(
	    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
	    columns=['lat', 'lon'])

	
	chart = alt.Chart(mf.dayBreakdown(sneezeData2020)).mark_bar().encode(
		x=alt.X('Day of Week:N', sort=None),
		y=alt.Y('Daily Sum:Q',scale=alt.Scale(domain=[0,300])),
		color=alt.Color('Day of Week')
	).properties(width=alt.Step(100))

	st.write(map_data)
	st.altair_chart(chart)
	st.write(sneezeData2020)


