import os
from json import dumps
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')


@app.route("/")
def index():
    return render_template('cmd.html')


@app.route("/cmd")
def cmd():
    osname = os.uname()[3]
    print(osname)
    return dumps({'name': osname})


if __name__ == "__main__":
    app.run()
