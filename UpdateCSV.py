import os.path
import requests
import gspread
import pandas
import numpy as np

if (os.path.isfile("sneezes2021.csv") & os.path.isfile("sneezes2021.csv")):	
	gc = gspread.service_account(filename='service_account.json')
	worksheet = gc.open('2020 Sneeze Survey')
	array1 = np.array(worksheet.sheet1.get_all_values())
	

	worksheet = gc.open('2021 Sneeze Survey')
	array2 = np.array(worksheet.sheet1.get_all_values())
	array3 = np.append(array2,array1)
	np.savetxt("sneezes2020.csv",array1,delimiter=";",fmt='%s')	
	np.savetxt("sneezes2021.csv",array2,delimiter=";",fmt='%s')
	np.savetxt("allSneezes.csv",array3,delimiter=";",fmt='%s')