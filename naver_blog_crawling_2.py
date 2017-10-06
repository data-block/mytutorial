# 라이브러리 호출
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 함수 정의
def search_naver_blog(keyword, page):
    start = (page-1)*10 + 1
    get_url = lambda keyword, start: "https://search.naver.com/search.naver?where=post&query={keyword}&start={start}".format(
        keyword=keyword, start=start
        )
    print("크롤링 키워드: " + keyword + " / " +"크롤링 페이지: " + str(page))
    print("크롤링 url: " + get_url(keyword, start))

    requests_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=AskDjango'
    }

    response = requests.get(get_url(keyword, start), headers=requests_headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    post_elements = dom.select(".sh_blog_top")

    result = [
        {
            "title": post_element.select_one(".sh_blog_title").text,
            "url": post_element.select_one(".sh_blog_title").attrs.get("href"),
            "date": post_element.select_one(".txt_inline").text.spilit()[0],
            "description": post_element.select_one(".sh_blog_passage").text,
            "blog_name": post_element.select_one(".txt84").text
        }
        for post_element
        in post_elements
    ]

    df = pd.DataFrame(result, columns=["title", "blog_name", "description", "url"])
    return(df)
    

# 요청
search_naver_blog("keyword", page_no)