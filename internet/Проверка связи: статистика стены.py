import requests, json

domain = 'm_sosin04'
count = 100
token = '5914e9cf5914e9cf5914e9cf4159715e63559145914e9cf026dd056a192cf6e3c749885'

url = "https://api.vk.com/method/wall.get?domain={}&count={}&access_token={}&v=5.74".format(domain, count, token)

response = requests.get(url)
answer = json.loads(response.text)
i=0
for post in answer['response']['items']:
    i+=1
    print('Пост номер -', i)
    print(' Кол-во лайков - ', post['likes']['count'])
    print(' Кол-во комментариев - ', post['comments']['count'])
    print('')
