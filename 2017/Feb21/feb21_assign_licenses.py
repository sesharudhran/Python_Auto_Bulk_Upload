import csv
import json
import httplib, urllib
import requests


#Assign License to below School
schoolId = "5633a601a139852b08f80ff9"

#Feed File
csvfilename = 'feb21_feedfile.csv'
output = []
row_count = 0
field_count = 0

csvfile = open(csvfilename, 'rU')
fieldnames = ('product_id','title','coverImageURL')
reader = csv.DictReader(csvfile, fieldnames)

#qa api url
# productURL = "https://api-qa.gls.pearson-intl.com/product"
# addLicenseURL = "https://api-qa.gls.pearson-intl.com/license"

#prod api url
addLicenseURL = "https://api-prod.gls.pearson-intl.com/license"

#qa headers
# headers = {"content-type": "application/json; charset=UTF-8",
#              "appid": "555db1225658d59af24baa34",
#              "token": "OTM3ZDhkNmYtNmVkYi00MGViLTlmNWUtMDEwMDE1NjFlZmI2OjoxNDQ4MzYzNjA4NTQ4OnNEa2poZmtqOHlobjhnaWc="}

#prod headers
headers = {"content-type": "application/json; charset=UTF-8",
             "appid": "54c89f6c1d650fdeccbef5cd",
             "token": "QVFJQzV3TTJMWTRTZmN3T1FLZTFpSGpRMnhXdklBLW9VWk44ZUJIZ2l0b2F6cm8uKkFBSlRTUUFDTURJQUFsTkxBQk0wTlRVMk1qTTNNamsyTURJM05USTVOVGMwQUFKVE1RQUNNRGMuKjo6MTQ4NzY5MzQzNzE4MTpzRGtqaGZrajh5aG44Z2ln"}

# My School QA
# schoolId = "559cf49c6dd48154057541e6"

# Prod school name - QA School :56659394c2ce755608f7a832



responsefilename = csvfilename.split('.')[0] +'_Response_dump.json'
responsedump = open(responsefilename, 'w')

first_row = next(reader)
for row in reader:
	row_count = row_count + 1
	
# 	Add License to School
	payload = {}
	productId = row['product_id']
# 	print productId
	payload['product'] = productId
	payload['school'] = schoolId
	payload['seats'] = '1000'
	payload['start'] = '2017-01-01T16:46:07+00:00'
	payload['end'] = '2099-12-31T16:46:07+00:00'
	
	addLicenseRequest = json.dumps(payload)
	

	print '**************** addLicenseRequest ****************' 
	print row_count
# 	print addLicenseRequest

  	licenseResponse = requests.post(addLicenseURL, headers=headers, data=addLicenseRequest)
	print "Adding License ..."
	print licenseResponse.status_code
	print "\n"
	print licenseResponse.content

# 	responsedump.write(row_count)
# 	responsedump.write(licenseResponse.status_code)
	ResCode = licenseResponse.status_code
	responsedump.write(str(ResCode))
	responsedump.write(licenseResponse.content)

	responsedump.write(" \n --------------------------------------------------------- \n")
