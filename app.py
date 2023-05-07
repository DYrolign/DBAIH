from flask import *
from flask_cors import *

app = Flask(__name__)


@app.route('/me')
def index():
    return redirect('https://dongbob-1011.github.io/home/')


@app.route('/')
def home():
    return redirect('/home')


@app.route('/home')
def homepage():
    t = ' - Home - '
    msg = 'Hello World'
    return render_template('home.html', data=msg, title=t)


@app.route('/download')
def downloadpage():
    t = ' - Download - '
    return render_template("download.html", title=t)


if __name__ == '__main__':
    app.run(debug=True)
    CORS(app)
