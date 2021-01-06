import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
#with open(os.path.join('C:\\Users\\Gage\\Downloads\\sneezeAnalysis-master\\sneezeAnalysis-master','Sneezes.csv')) as csvFile:
sneezeData2020 = pd.read_csv('sneezes2020.csv')
sneezeData2021 = pd.read_csv('sneezes2021.csv')
def app():
	st.title('Analysis of 2021 Sneezes')
	st.write('Shortcomings')
	if st.button('Click for sum'):
		st.write(totalCount(sneezeData2021))


def printLine():
	st.write("farts")

#gets the sum of all the values in the sneezes column
def totalCount(sneezedata):
	sneezeSum=sneezedata.sum(axis=0)
	return sneezeSum[1]




	st.write(sneezeData2021)
	print('fart')