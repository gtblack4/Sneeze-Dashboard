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
		cols[0].write("Days Without Sneezes:")
		cols[1].write(mf.sneezeLessDays(sneezeData2020))

	timeFrame = st.beta_columns(2)
	timeFrame[0].write(mf.dayBreakdown(sneezeData2020))	
	timeFrame[1].write(mf.monthBreakdown(sneezeData2020))




	st.write(sneezeData2020)


