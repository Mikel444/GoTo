from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<HTML>
<head>
	<title>Amigo_memory</title>
</head>
<body  bgcolor="green">
<text size="250px"
color = HEX(ffffff)>
#AMIGO_is_living
</text>
<img src = "amigo-mail.jpg">
"amigo-mail.jpg"
<img/amigo-mail.jpg>
<h1>
<text size="250px"
color = black>
If you press 
</text>
<a href = "https://media.cdnandroid.com/76/09/e8/c2/imagen-amigo-web-browser-0big.jpg">
here
</a>
</text>
<text size="250px"
color = black>
, Amigo
</text>
<text size="300px"
color = ff0000>
WON'T
</text>
<text size="250px"
color = black>
Download
</text>
<table>
	<tr>
		<th>A<th>
		<th>M<th>
	</tr>
	<tr>
		<td>I<td>
		<td>G<td>
	</tr>
	<tr>
		<td>O<td>
		<td>:)<td>
	</tr>
</table>
</body>
</HTML>'''

@app.route('/about')
def about():
    return """
<html>
    <body>
    <body  bgcolor="blue">
        Это страница о сервисе!
        Амиго всё таки ЖИВ!
    </body>
</html>
"""

app.run(debug=True, port=8080)
