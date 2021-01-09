import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import csv
import twentytwenty
import twentytwentyone
import about
import dashboard
import requests
import gspread
import os.path
import functions as mf
def main():
	sneezeData2020 = pd.read_csv('sneezes2020.csv',sep=";") #.dropna()
	sneezeData2021 = pd.read_csv('sneezes2021.csv',sep=";") #.dropna()

	st.title("Gage's Sneeze Collection Project")

	PAGES = {
		"Dashboard": dashboard,
		"About The Project": about,
		"2020 Data and Analysis": twentytwenty,
		"2021 Data and Analysis": twentytwentyone

	}
	st.sidebar.title('Navigation')
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))


	page = PAGES[selection]
	

#For now, if the file doesn't exist. We will retreive it from Google.
#TODO Check if the file was created in the last week
	if not (os.path.isfile("sneezes2020.csv")):
		gc = gspread.service_account(filename='service_account.json')
		worksheet = gc.open('2020 Sneeze Survey')
		array = np.array(worksheet.sheet1.get_all_values())
		np.savetxt("sneezes2020.csv",array,delimiter=";",fmt='%s')
	if not (os.path.isfile("sneezes2021.csv")):
		gc = gspread.service_account(filename='service_account.json')
		worksheet = gc.open('2021 Sneeze Survey')
		array = np.array(worksheet.sheet1.get_all_values())
		np.savetxt("sneezes2021.csv",array,delimiter=";",fmt='%s')
	
	page.app()
if __name__ == '__main__':
	main()

