from flask import Flask, request, redirect
from caesar import encrypt
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

# Global Variables
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post"
        <label for="rotate">Rotate by: </label>
        <input name="rot" type="text" value="0" size="35" /><br>
        <textarea name="text" rows="4" cols="50">{0}</textarea>
        <input name="submit_button" type="submit" value="Submit Query" />
      </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form.format('')


@app.route("/", methods=['POST'])
def rotate_string():
    rot = request.form['rot']
    text = request.form['text']
    answer = ""

    rot = cgi.escape(rot)
    text = cgi.escape(text)

    rot = int(rot)

    answer = encrypt(text, rot)

    return '<h1>'+ form.format(answer) + '</h1>'


app.run()