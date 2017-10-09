## 1. 라이브러리 호출
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


## 2-1. 사전 전처리1
lines = '''pageInfo:bksMain
login_chk:null
LOGIN_SN:null
LOGIN_NAME:null
indexName:news
keyword:빅데이터
byLine:
searchScope:1
searchFtr:1
startDate:2017-07-09
endDate:2017-10-09
sortMethod:score
contentLength:100
providerCode:
categoryCode:
incidentCode:
dateCode:
highlighting:true
sessionUSID:
sessionUUID:test
listMode:
categoryTab:
newsId:
delnewsId:
delquotationtxt:
filterProviderCode:
filterCategoryCode:
filterIncidentCode:
filterDateCode:
filterAnalysisCode:
startNo:1
resultNumber:100
topmenuoff:
resultState:
keywordJson:
keywordFilterJson:
realKeyword:
totalCount:
interval:
quotationKeyword1:
quotationKeyword2:
quotationKeyword3:
searchFromUseYN:N
mainTodayPersonYn:
period:3month
sectionDiv:'''.splitlines()


## 2-2. 사전 전처리2
data = {}
for line in lines:
    key, value = line.split(':', 1)
    if value == 'null':
        value = None
    print(key, value)
    data[key] = value
# data


## 3. url 요청
result_url = "https://www.bigkinds.or.kr/news/newsResult.do"
response = requests.post(result_url, data=data)
# response

## 4. html parsing
html = response.text
soup = BeautifulSoup(html, 'html.parser')

## 5. title, id, description 추출
result = []
for tag in soup.select('.resultList li a'):
#     print(tag)
#     print()
    main_tag = tag.select('h3')
    description_tag = tag.select('p')
    
    for tag in main_tag:
        doc_id = tag['id'].replace('news_', '')
        title = tag.text.strip()
        doc_url = 'https:/www.bigkinds.or.kr/news/detailView.do?docId={}&returnCnt=1&sectionDiv=1000'.format(doc_id)
#         print("doc id:", tag['id'].replace('news_', ''))
#         print("title:", tag.text.strip())
    for tag in description_tag:
#         print("description:", tag.text)
#         print()
        description = tag.text

        result.append({'doc_id': doc_id,
                   'title': title,
                   'description': description
                  })
        df = pd.DataFrame(result, columns=['title', 'description', 'doc_id', 'doc_url'])

## 6. DataFrame
df

## 7. json loads

## 8. original link