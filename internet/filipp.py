import requests, json

domain = 'kinopoisk'
token = '5914e9cf5914e9cf5914e9cf4159715e63559145914e9cf026dd056a192cf6e3c749885'

url = 'https://api.vk.com/method/wall.get?domain={}&count=1&access_token={}&v=5.80'.format(domain,token)

response=requests.get(url)
answer=json.loads(response.text)
count=answer["response"]["count"]

print(count)
win_post=''
likes_max=0
for offset in range(0,count,100):
    print(offset)
    url='https://api.vk.com/method/wall.get?domain=kinopoisk&count..{}&access_token={}&v=5.80'.format(offset,token)
    response=requests.get(url)
    answer=json.loads(response.text)
    for post in answer["response"]["items"]:
        likes=post["likes"]["count"]
        if likes>likes_max:
            likes_max=likes
            win_post=post["text"]
print(win_post)
print(likes_max)

