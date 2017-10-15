

### 1
## 도전 1

import requests
from bs4 import BeautifulSoup

url_1 = "https://www.ftc.go.kr/info/dataopen/openVisitList.jsp"
response_1 = requests.post(url_1, data=data)
response_1

### 2
## ssl 인증 에러가 뜸
## 도전 2
import ssl

context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context
url_2 = "https://www.ftc.go.kr/info/dataopen/openVisitList.jsp?schCheck=&menu_id=01"

response_2 = requests.post(url_2, data=data, context=context)
response_2

### 3
## Type 에러가 뜸
#  TypeError: request() got an unexpected keyword argument 'context'
## 도전3
import urllib.request

resp = urllib.request.urlparse(url_2)
resp

response_3 = requests.post(url_2, data=data, context=context)
response_3