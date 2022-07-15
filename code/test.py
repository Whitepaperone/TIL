from urllib import response
import requests

url='https://api.agify.io/?name=michael'
response =requests.get(url).json()

print(response.get('name'))

print(response['age'])