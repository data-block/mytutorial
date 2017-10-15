
'''
[개요1 - 필요한 자료에 대한 설명]
- 1. 공정거래위원회 사업자 정보 다운로드

> - 1-1. 17개 시도, 243개의 시군구 자료 다운로드

> - 1-2. 사업자1 (3종): 통신판매, 방문판매, 전화권유판매 사업자 ★ 이 부분을 자동화시켜야 함!

> - 1-3. 사업자2 (2종): 다단계, 선불식할부거래 사업자 ... 한 번에 직접 다운로드 가능


[개요2 - 홈페이지 방식]
- 2. (1-2의 사업자1 3종) GET + POST + javascript 방식으로 구현

 > - 2-1. 사업자 카테고리를 선택해도 get 방식
 
 > - 2-2. 지역1(시도)을 선택하면 post 방식으로 넘어감
 
 > - 2-3. 지역2(시군구)를 선택해도 network 탭에서는 새로운 반응이 없음
 
 > - 2-4. 다운로드 버튼은 자바스크립트로 구현 (url이 없음)

[개요3 - url 및 인자에 대한 설명]
- 3-1. url
 > - https://www.ftc.go.kr/info/dataopen/openVisitList.jsp

- 3-2. post_url (예시)
 > - ?schCheck=&menu_id=03&area1=6260000&area2=3000000

- 3-3. post 인자
 > - 3-3-1. menu_id: 사업자
  >> - 01: 통신판매사업자 ★
   >>> - schCheck=&menu_id=01&area1=6110000&area2=

  >> - 03: 방문판매사업자 ★

  >> - 04: 전화권유판매사업자 ★

 > - 3-3-2. area1: 17개의 시도

 > - 3-3-3. area2: 243개의 시군구

'''

### 1
## 도전 1
import requests
from bs4 import BeautifulSoup

url_1 = "https://www.ftc.go.kr/info/dataopen/openVisitList.jsp"
response_1 = requests.post(result_url, data=data)
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