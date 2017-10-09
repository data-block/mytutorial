# 1. 라이브러리 호출
import requests
from bs4 import BeautifulSoup
import pandas as pd


# 2. 함수 정의_1
def crawl_naver_webtoon_1(page):
    list_url = 'http://comic.naver.com/webtoon/list.nhn'
    params = {
        'titleId': 651673,  # 유미의 세포들 id
        'page': page
    }

    html = requests.get(list_url, params=params).text
    soup = BeautifulSoup(html, 'html.parser')
    result = []
    
    for tag in soup.select(".viewList tr"):
        title_url_tag_list = tag.select('.title a')
        rating_tag_list = tag.select('.rating_type')
        for tag in title_url_tag_list:
            title = tag.text
            url = 'http://comic.naver.com/'+tag.get('href')
            print(title)
            print(url)
        for tag in rating_tag_list:
            rating = tag.text.split()[1]
            print(rating)
            result.append({
                'title': title,
                'url': url,
                'rating': rating
            })
            df1 = pd.DataFrame(result, columns=['title', 'url', 'rating'])
    return(df1)


# 3. 함수 정의_2
def crawl_naver_webtoon_2(j):
    df = pd.DataFrame()
    for i in range(1, j + 1):
        page = i
        print("download webtoon:", )
        print("donwload page:", page)
        get_data = crawl_naver_webtoon_1(i)
        df = df.append(get_data, ignore_index=True)
    return(df)

# 4. 호출
crawl_naver_webtoon_2(page)