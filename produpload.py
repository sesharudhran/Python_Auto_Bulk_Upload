import csv
import json
import httplib, urllib
import requests

csvfilename = 'van_csv.csv'
output = []
row_count = 0
field_count = 0

csvfile = open(csvfilename, 'rU')
fieldnames = ('description','title','allowedPageNavigation','layout','epubURL','coverImageURL')
reader = csv.DictReader(csvfile, fieldnames)

#qa api url
# productURL = "https://api-qa.gls.pearson-intl.com/product"
# addLicenseURL = "https://api-qa.gls.pearson-intl.com/license"

#prod api url
productURL = "https://api-prod.gls.pearson-intl.com/product"
addLicenseURL = "https://api-prod.gls.pearson-intl.com/license"

#qa headers
# headers = {"content-type": "application/json; charset=UTF-8",
#              "appid": "555db1225658d59af24baa34",
#              "token": "OTM3ZDhkNmYtNmVkYi00MGViLTlmNWUtMDEwMDE1NjFlZmI2OjoxNDQ4MzYzNjA4NTQ4OnNEa2poZmtqOHlobjhnaWc="}

#prod headers
headers = {"content-type": "application/json; charset=UTF-8",
             "appid": "54c89f6c1d650fdeccbef5cd",
             "token": "YzM4NDRmMzUtODUzNy00ZmFkLWIxYTAtODNiMzFkMTk1ZTZlOjoxNDQ5NDk3OTMxNzc0OnNEa2poZmtqOHlobjhnaWc="}

# My School QA
# schoolId = "559cf49c6dd48154057541e6"

# Prod school name - QA School :56659394c2ce755608f7a832

schoolId = "5633a694a139852b08f80fff"

responsefilename = csvfilename.split('.')[0] +'_Response_dump.json'
responsedump = open(responsefilename, 'w')

first_row = next(reader)
for row in reader:
	row_count = row_count + 1
	jsonfilename = csvfilename	.split('.')[0] + str(row_count) +'_Request.json'
	jsonfile = open(jsonfilename, 'w')
	json.dump(row, jsonfile)
	print "Request Json created for Product:" + str(row_count)
# 	print json.dumps(row)

#	Create product	
	response = requests.post(productURL, headers=headers, data=json.dumps(row))
	print "---------------------------Response ----------------------------------"
	print response.status_code	
 	print response.content
	print "----------------------------------------------------------------------"
	print "Response dump populated ..."
	print "\n"
	responsedump.write(response.content)
	
	responseText = json.loads(response.text)
	productId = responseText['id']
# 	print productId
	
# 	Add License to School
	payload = {}
	payload['product'] = productId
	payload['school'] = schoolId
	payload['seats'] = '1000'
	payload['start'] = '2015-12-15T16:46:07+00:00'
	payload['end'] = '2099-12-31T16:46:07+00:00'
	
	addLicenseRequest = json.dumps(payload)

# 	print 'addLicenseRequest****************' 
# 	print addLicenseRequest

 	licenseResponse = requests.post(addLicenseURL, headers=headers, data=addLicenseRequest)
	print "Adding License ..."
	print licenseResponse.status_code
	print "\n"
	print licenseResponse.content
	
	responsedump.write(" \n --------------------------------------------------------- \n")
