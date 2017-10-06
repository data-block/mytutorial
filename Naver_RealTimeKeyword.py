import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('http://naver.com').text
soup = BeautifulSoup(html, 'html.parser')
tag_list = soup.select('.PM_CL_realtimeKeyword_base .ah_item .ah_k')

result = []

for tag in tag_list:
    realtimekeyword = [tag.text]
    result.append(realtimekeyword)

df = pd.DataFrame(result, columns=['keyword'])
df