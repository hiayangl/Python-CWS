# -*- coding: utf-8 -*-

import requests
import json

#authentication
url='http://dlw-ecmdemo.chinaeast.cloudapp.chinacloudapi.cn/otcs/llisapi.dll/api/v1/auth'
payload = {'username': 'admin', 'password': 'Ecm1234!'}
response = requests.post(url,data=payload)
jData = json.loads(response.content)
print(jData['ticket'])

nodeID = r'566775'

#downloading file
headers = {'otcsticket': jData['ticket']}
url='http://dlw-ecmdemo.chinaeast.cloudapp.chinacloudapi.cn/otcs/llisapi.dll/api/v1/nodes/'+ nodeID + '/content'
response = requests.get(url,data=payload,headers=headers)
print(response.status_code)

filePath = r'D:\Python\test.docx'
f = open(filePath, 'wb')
f.write(response.content)
f.close()