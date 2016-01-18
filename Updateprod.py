import csv
import json
import httplib, urllib
import requests
import yaml

csvfilename = 'update_durban_csv1.csv'
output = []
row_count = 0
field_count = 0

csvfile = open(csvfilename, 'rU')
fieldnames = ('id','epubURL','coverImageURL')
reader = csv.DictReader(csvfile, fieldnames)

#qa api url
# productURL = "https://api-qa.gls.pearson-intl.com/product/"

#prod api url
productURL = "https://api-prod.gls.pearson-intl.com/product/"


#qa headers
# headers = {"content-type": "application/json; charset=UTF-8",
#              "appid": "555db1225658d59af24baa34",
#              "token": "OTM3ZDhkNmYtNmVkYi00MGViLTlmNWUtMDEwMDE1NjFlZmI2OjoxNDQ4MzYzNjA4NTQ4OnNEa2poZmtqOHlobjhnaWc="}

#prod headers
headers = {"content-type": "application/json; charset=UTF-8",
              "appid": "54c89f6c1d650fdeccbef5cd",
              "token": "YzM4NDRmMzUtODUzNy00ZmFkLWIxYTAtODNiMzFkMTk1ZTZlOjoxNDQ5NDk3OTMxNzc0OnNEa2poZmtqOHlobjhnaWc="}


responsefilename = csvfilename.split('.')[0] +'_Response_dump.json'
responsedump = open(responsefilename, 'w')

first_row = next(reader)
for row in reader:
	row_count = row_count + 1
	jsonfilename = csvfilename.split('.')[0] + str(row_count) +'_Request.json'
	jsonfile = open(jsonfilename, 'w')
# 	json.dump(row, jsonfile)
# 	print "Request Json created for Product:" + str(row_count)
 	payload = json.dumps(row)
#   	print payload
# 	payloadTrim = json.loads(payload)
	payloadTrim1 = yaml.load(payload)
	
# 	print payloadTrim["id"]
  	updateProductURL = productURL + payloadTrim1["id"]
	print updateProductURL
#  	print prodID['id']
	
	del payloadTrim1["id"]
# 	print payloadTrim1
	updatedPayLoad = json.dumps(payloadTrim1)
# 	print updatedPayLoad

	print "\n"
# 	print "-------------------------------------------------------\n"

#	Update product	
 	response = requests.put(updateProductURL, headers=headers, data=updatedPayLoad)
 	print "---------------------------Response ----------------------------------"
 	print response.status_code	
  	print response.content
 	print "----------------------------------------------------------------------"
 	print "Response dump populated ..."
 	print "\n"

 	responsedump.write(response.content)
 	responseText = json.loads(response.text)
 	productId = responseText['id']
 	
 	responsedump.write(" \n --------------------------------------------------------- \n")
