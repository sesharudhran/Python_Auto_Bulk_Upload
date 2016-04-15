import csv
import json
import requests
from Tkinter import Tk
from tkFileDialog import askopenfilename

row_count = 0
headers = {};

def user_selection():
	Add_School_API = ""

	env_Selection = {'qa':'https://api-qa.gls.pearson-intl.com:443/school','stg':'https://api-stg.gls.pearson-intl.com/school', 'prod':'https://api-prod.gls.pearson-intl.com/school'}
	
	Env = raw_input("Select Env for provisioning: ")
	global Env
	countryCode = raw_input("Enter Country code e.g TR: ")
	global countryCode
# 	print (Env)
# 	print (countryCode)
	
	try:
		Add_School_API = env_Selection[Env]
# 		api_header = header_Selection[Env]
# 		print Add_School_API
# 		headers = api_header
# 		print "******************* inside method ******************"
# 		print headers
		return Add_School_API
	except KeyError:
		print ("Env %s not found" % Env )
     	exit(0)	

def file_select():	
	
	Tk().withdraw()
	wfilename = askopenfilename() 
# 	print(wfilename)

	if wfilename.endswith('.csv'):
		print "valid csv"
		return wfilename
	else:
		print "Please select a valid csv file"
		exit(0)

def header_select(env_header):
	header_Selection = {'qa':{"content-type": "application/json; charset=UTF-8",
								 "appid": "56fe4441484f51cd68b98544",
								 "token": "ODg0NjUzNjMtMjIyOC00ZTQ5LWJiYjQtYmY5YTU0YWQyM2ExOjoxNDU3MzU1ODQxMTE2OnNEa2poZmtqOHlobjhnaWc="},
						 'stg':'https://api-stg.gls.pearson-intl.com/school', 						 
						 'prod':{"content-type": "application/json; charset=UTF-8",
								 "appid": "54c89f6c1d650fdeccbef5cd",
								 "token": "YzM4NDRmMzUtODUzNy00ZmFkLWIxYTAtODNiMzFkMTk1ZTZlOjoxNDQ5NDk3OTMxNzc0OnNEa2poZmtqOHlobjhnaWc="}
						}

	
	try:
		api_header = header_Selection[env_header]
#  		print ("api_header --------->")
# 		print (api_header)
		return api_header
	except KeyError:
		print ("env_header %s not found" % env_header )
     	exit(0)	
    
env_selected = user_selection()
file_path = file_select()
headers = header_select(Env)

# print "******************* OUTSIDE method ******************"
# print headers

# print "ENV"
# print Env
# print "headers ------------------------->"
# print headers	

# print file_path


def open_csv():
	csvfile = open(file_path, 'rU')
	fieldnames = ('schoolname','', '')
	reader = csv.DictReader(csvfile, fieldnames)
	first_row = next(reader)
	row_count = 0

	 
	outputFileName = open('School_Upload_Output.csv', 'w')

	outputWriter = csv.writer(outputFileName)
	outputWriter.writerow(['school_id'])

	for row in reader:
		row_count = row_count + 1
# 		print row_count
		print row['schoolname']


		payload = {}
		payload['countryCode'] = countryCode
		payload['name'] = row['schoolname']

		addSchoolRequest = json.dumps(payload)
			
		response = requests.post(env_selected, headers=headers, data=addSchoolRequest)
	
		print "---------------------------Response ----------------------------------"
		print response.status_code	
		print response.content
	
		print "----------------------------------------------------------------------"
		print "Response dump populated ..."
		print "\n"
# 		responsedump.write(response.content)
		responseText = json.loads(response.text)	
		schoolId = responseText['id']
		
		outputWriter.writerow([schoolId])
		
	outputFileName.close()

open_csv()	





