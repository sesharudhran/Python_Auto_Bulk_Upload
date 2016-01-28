import csv
import json
import httplib, urllib
import time
import requests
import datetime




#Authenticate api url
authURL = "https://api-prod.gls.pearson-intl.com/authenticate"
userName = "balaji@demo.com"
password = "hudson102"

# get user api URL

userURL = "https://api-prod.gls.pearson-intl.com/user"

payload = {}

payload['username'] = 'balaji@demo.com'
payload['password'] = 'hudson102'

#prod headers

headers = {"content-type": "application/json; charset=UTF-8","appid": "54c89f6c1d650fdeccbef5cd"}

now = datetime.datetime.now()
responsefilename = "Session_Expiry_Log_"+ now.isoformat() +".log"
# responsefilename = "Session_Expiry_Log"+ now.isoformat() +".txt"
responsedump = open(responsefilename, 'w')

response = requests.post(authURL, headers=headers, data=json.dumps(payload))
print "--------------------------- Authenticate Response ----------------------------------"
time.ctime()
print "Start Time:" + time.strftime('%l:%M%p %z on %b %d, %Y')
print response.status_code	
print response.content
print "----------------------------------------------------------------------"
print "\n"

responseText = json.loads(response.text)
responsedump.write("Start Time:")
responsedump.write(time.strftime('%l:%M%p %z on %b %d, %Y'))
responsedump.write("\n")
responsedump.write(response.content)
responsedump.write(" \n --------------------------------------------------------- \n")
tokenID = responseText['token']

# print "********"
# print tokenID

userHeader = {}
# userHeader['content-type'] = 'application/json; charset=UTF-8'

def validate_session():
	
	userHeader['token'] = tokenID
	userHeader['appid'] = '54c89f6c1d650fdeccbef5cd'
# 	print "---------------"
# 	print "Variable Type : %s" %  type (userHeader)
	userResponse = requests.get(userURL, headers=userHeader)
	print "---------------------------Response ----------------------------------"
	time.ctime()
	print "Latest Time:" + time.strftime('%l:%M%p %z on %b %d, %Y')
	print userResponse.status_code	
	print userResponse.content
	responsedump.write(time.strftime('%l:%M%p %z on %b %d, %Y'))
	responsedump.write("\n")
	responsedump.write(userResponse.content)
	print "----------------------------------------------------------------------"
	print "\n"
	responsedump.write(" \n --------------------------------------------------------- \n")
	if userResponse.status_code == 200:
# 		print tokenID
		print "session valid....."
		time.sleep(600)
	else:
		print "session invalid"
		exit()
	
while True:
	validate_session()
