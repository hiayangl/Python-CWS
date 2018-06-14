# -*- coding: utf-8 -*-

from zeep import Client
from zeep import xsd
import os

authClient = Client('http://dlw-ecmdemo.chinaeast.cloudapp.chinacloudapi.cn:8080/cws/services/Authentication?wsdl')
print('Authenticating User...')
token = authClient.service.AuthenticateUser('otadmin@otds.admin', 'Ecm1234!')
print('SUCCESS!')
print('token = ' + token)

docManClient = Client('http://dlw-ecmdemo.chinaeast.cloudapp.chinacloudapi.cn:8080/cws/services/DocumentManagement?wsdl')

header = xsd.Element(
            '{urn:api.ecm.opentext.com}OTAuthentication',
            xsd.ComplexType([
                xsd.Element(
                    '{urn:api.ecm.opentext.com}AuthenticationToken', 
					xsd.String()),
            ])
        )

header_value = header(AuthenticationToken=token)

#result = docManClient.seAuthenticationTokenrvice.GetNode('2000', _soapheaders=[header_value])
print('Generating context ID...')
nodeID = 690852
result = docManClient.service.GetVersionContentsContext(nodeID, 0, _soapheaders=[header_value])
#print(result)
contextID = result.__getitem__('body').__getitem__('GetVersionContentsContextResult')
print('SUCCESS!')
print('contextID = ' + contextID)
contentServiceClient = Client('http://dlw-ecmdemo.chinaeast.cloudapp.chinacloudapi.cn:8080/cws/services/ContentService?wsdl')
print('Downloading file...')
result = contentServiceClient.service.DownloadContent(contextID, _soapheaders=[header_value])
#print(result)
fileStream = result.__getitem__('body').__getitem__('DownloadContentResult')
filePath = r'D:\Python\test.zip'
f = open(filePath, 'wb')
f.write(fileStream)
f.close()
print('SUCCESS!')
fileSize = os.path.getsize(filePath)
#print(fileSize)
print('Downloaded ' + str(fileSize) + ' bytes to ' + filePath + '.')