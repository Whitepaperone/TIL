import requests

num='1014'
url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+num
response =requests.get(url).json()

for i in range(6):
    print(str(response.get(f'drwNo'))+'회차의 번호는 '+ str(response.get(f'drwtNo{i+1}')) + '입니다.')
print('보너스 번호는' + str(response.get(f'bnusNo'))+'입니다')