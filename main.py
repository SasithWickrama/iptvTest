import re
from datetime import time
import xml.etree.ElementTree as ET
import requests

iptvend='http://172.25.16.42:8082/tbms/services/TPEWebService.TPEWebServiceHttpSoap11Endpoint/'

xmlfile = open('IPTV_SUNT_SUSPEND.xml', 'r')
data = xmlfile.read()

response = requests.request("POST", iptvend, data=data)           
#print(response.content)

ResultCode = re.findall("<ax225:abstractServiceObjects xsi:type=\"ax222:AbstractServiceObject\">(.*?)</ax225:abstractServiceObjects>", str(response.content))
print(ResultCode[0])
ResultCode1 = re.findall("<ax222:value>(.*?)</ax222:value>", str(ResultCode[0]))
print(ResultCode1[0])
ResultCode2 = re.findall("<ax222:value>(.*?)</ax222:value>", str(ResultCode[1]))
print(ResultCode2[0])

root = ET.fromstring(response.content)

for record in root.iter('ax225:abstractServiceObjects xsi:type="ax222:AbstractServiceObject"'):
    print(record)
    for resultval in record.iter('ax222:fieldId'):
        print('resultval '+ resultval.text)
        if resultval.text == 1200:
            for resultcd in record.iter('ax222:value'):
                ResultCode = resultcd.text
                print(ResultCode)

        if resultval.text == 1201:
            for resultdes in record.iter('ax222:value'):
                ResultDesc = resultdes.text
                print(ResultDesc)
                            