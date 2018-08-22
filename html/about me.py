from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '''<HTML>
<body>

<body  bgcolor="yellow">

<center>
<text size="450px"
color = black>
<h1>
МОЙ САЙТ :) 
</h1>
</text>
</center>

<left>
<text size="250px"
color = black>
Сотрудники:
</text>
<br>
<a href="http://127.0.0.1:8080/Winnie_Puh">
1.Винни Пух
</a>
<br>
<a href="http://127.0.0.1:8080/Pyatochok">
2.Пяточок
</a>
<br>
#
#
<br>
Создатель: 
<a href="http://127.0.0.1:8080/me">
Я
</a>
<br>
#
#
<br>
<br>
Если же мы вас не интересуем - 
<a href="http://127.0.0.1:8080/weather">
Здесь
</a>
<br>
 вы можете узнать "САМУЮ ТОЧНУЮ И ПРАВДИВУЮ" погоду.
</left>

<right>
<img src="/static/amigo-mail.jpg" height="375" width="600">
</right>

<right>
<b>
<text size="100px"
color = black>
Наш спонсор: Amigo, которого нет. 
</text>
</b>
</right>

<body>
<HTML>'''

@app.route('/Winnie_Puh')
def Vinnie():
    return '''<HTML>
<body>
<body  bgcolor="red">
<right>
<img src="/static/Vinnue.jpg" height="225" width="300">
</right>
<br>
<b>
<text size="250px"
color = black>
Винни Пух
<br>
</text>
</b>
<br>
<left>
Имя: Винни <br>
Фамилия: Пух <br>
Кличка: Пух <br>
Порода: Медведь Обыкновенный <br>
<br>
Таланты.<br>
-Сочинение различного вида Фолклора <br>
-Поедание Мёда <br>
<br>
Особые приметы. <br>
-Опилки в голове <br>
<br>
Осторожно: может улететь!
<br>
</text>
</left>
<right>
<a href="http://127.0.0.1:8080/">
Main Screen
</a>
</right>
<body>
<HTML>'''

@app.route('/Pyatochok')
def Pyatachok():
    return '''<HTML>
<body>
<body  bgcolor="red">
<right>
<img src="/static/Pyatachok.jpg" height="225" width="300">
</right>
<b>
<text size="250px"
color = black>
Пяточок
<br>
</text>
<br>
</b>
<left>
Имя: Пяточок
<br>
Фамилия: -отсутствует-
<br>
Кличка: Пяточок
<br>
Порода: Поросёнок Обыкновенный
<br>
<br>
Таланты.
<br>
-Надувание шариков
<br>
-уничтожение шариков (в самый не подходящий момент)
<br>
-Меткий, стрельба из ружья.
<br>
<br>
Особые приметы.
<br>
-Пятак вместо носа
<br>
-Низкий
<br>
<br>
Осторожно: Вооружён и опасен!
</left>
<br>
<right>
<a href="http://127.0.0.1:8080/">
Main Screen
</a>
</right>
<body>
<HTML>'''

@app.route('/me')
def me():
    return '''<HTML>
<body>
<body  bgcolor="blue">
<b>
<text size="500px">
Создатель сайта.
</text>
</b>
<br>
</text>
<center>
<img src="/static/Ya.jpg" height="480" width="480">
</center>
<left>
<b>
<text size="150px"
color = black>
***Информация скрыта.***
</text>
</b>
</left>

<right>
<a href="http://127.0.0.1:8080/">
Main Screen
</a>
</right>
<body>
<HTML>'''

@app.route('/weather')
def weather():
    temperature = random.randint(-70,40)
    return '''<HTML>
<body>
<body  bgcolor="yellow">
<center>
<b>
<text size="500px"
color = black>
ПОГОДА
</text>
</b>
<br>
</center>
<left>
Погода на завтра обещает быть незабываемой!
<br>
В какой то момент столбики термометров достигнут отметки {} градусов по цельсию
</left>
<right>
<img src="/static/weather.jpg" height="300" width="500">
<a href="http://127.0.0.1:8080/">
Main Screen
</a>
</right>
<body>
<HTML>'''.format(temperature)

app.run(debug=True, port=8080)
