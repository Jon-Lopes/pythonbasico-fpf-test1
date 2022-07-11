import requests


res = requests.get('https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8')

print(res.json())