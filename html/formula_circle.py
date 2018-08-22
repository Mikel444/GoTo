from flask import Flask, request

app = Flask(__name__)

pi = 3.14

@app.route('/ScircleR')
def hello():
    global pi
    
    counting = "Я помогу вычислить площадь круга по его радиусу,<br> которая равна S = pi*R^2, <br> где S - площадь, pi - число пи, а R - заданный радиус этого круга"
    if "r" in request.args:
        try:
            R = float(request.args['r'])
            S = pi * R * R
            counting = "Площадь круга равна {}".format(S)
        except:
            pass

    return """
    <html>
        <body>
            <p>{}</p>

            <form action='/ScircleR' method='GET'>
                Radius: <input type="text" name="r" /><br>
                <input type="submit" value="ОК!" />
            </form>
        </body>
    </html>
    """.format(counting)

app.run(debug=True, port=8080)
