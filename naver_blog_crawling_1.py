import requests
from bs4 import BeautifulSoup
from itertools import count
import pandas as pd

def naver_blog_search(q):
    # url 설정
    url = "https://search.naver.com/search.naver"
    # 헤더 설정
    requests_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=AskDjango'
    }
    
    result = []
    # get 인자(크롤링할 조건들)
    params = {
        "where": "post",
        "query": q,
        "start": 1, # 1, 11, 21, 31, 41 ...
    }
    print(params)
    
    html = requests.get(url, params=params, headers=requests_headers).text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.sh_blog_title')

    for tag in tag_list:
        print(tag.text, tag['href'])

        title = tag.text
        url = tag['href']
        result.append({
            'title': title,
            'url': url
        })
        
    df = pd.DataFrame(result)
    return df


# 결과 수행 코드
result = naver_blog_search('AskDjango')
result