import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/sise/sise_index.naver?code=KOSPI'
response = requests.get(url).text
# print(response)
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#change_value_and_rate')
result = kospi.text
print(result)