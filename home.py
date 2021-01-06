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

def main():
	st.title("Gage's Sneeze Project")

	PAGES = {
		"Home Dashboard": dashboard,
		"About The Project": about,
		"2020 Data and Analysis": twentytwenty,
		"2021 Data and Analysis": twentytwentyone

	}
	st.sidebar.title('Navigation')
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))
	page = PAGES[selection]
	page.app()
if __name__ == '__main__':
    main()

