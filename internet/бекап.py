import requests

response = requests.get("https://habr.com")

file = open("response.html", 'w', encoding='utf-8')
file.write(response.text)
file.close

