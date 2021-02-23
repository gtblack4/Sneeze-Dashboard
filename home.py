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
favicon = 'favicon.png'
def main():
	st.set_page_config(page_title='The Sneeze Project', page_icon = favicon, layout = 'centered', initial_sidebar_state = 'auto')

	#st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">'+'Fart'+'</div>', unsafe_allow_html=True)
	sneezeData2020 = pd.read_csv('sneezes2020.csv',sep=";") #.dropna()
	sneezeData2021 = pd.read_csv('sneezes2021.csv',sep=";") #.dropna()


	

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

	# if (os.path.isfile("sneezes2020.csv")):
	# 	gc = gspread.service_account(filename='service_account.json')
	# 	worksheet = gc.open('2020 Sneeze Survey')
	# 	array = np.array(worksheet.sheet1.get_all_values())
	# 	np.savetxt("sneezes2020.csv",array,delimiter=";",fmt='%s')
	# if (os.path.isfile("sneezes2021.csv")):
	# 	gc = gspread.service_account(filename='service_account.json')
	# 	worksheet = gc.open('2021 Sneeze Survey')
	# 	array = np.array(worksheet.sheet1.get_all_values())
	# 	np.savetxt("sneezes2021.csv",array,delimiter=";",fmt='%s')
	
	page.app()
if __name__ == '__main__':
	main()

