import requests, json

domain = 'm_sosin04'
token = '5914e9cf5914e9cf5914e9cf4159715e63559145914e9cf026dd056a192cf6e3c749885'

url = 'https://api.vk.com/method/wall.get?domain={}&count=1&access_token={}&v=5.80'.format(domain,token)

response=requests.get(url)
answer=json.loads(response.text)
count=answer["response"]["count"]

print(count)
win_post=''
max_like=0
win_post = ''
for offset in range(0,count,100):
    print('Обработано ',offset,' постов')
    url = "https://api.vk.com/method/wall.get?domain={}&count=1&offset={}&access_token={}&v=5.74".format(domain, offset, token)
    response=requests.get(url)
    answer = json.loads(response.text)
    for post in answer['response']['items']:
        if post['likes']['count'] > max_like:
            max_like = post['likes']['count']
            win_post = post['text']

print('ПОСТ ПОБЕДИТЕЛЬ!')
print('(пост, на котором кнопка лайк была нажата наибольшее кол-во раз)')
print('')
print(win_post)
print('')
print(max_like,' лайков')

