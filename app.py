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
def home_page():
    t = ' - Home - '
    msg = 'Guten Morgen!'
    return render_template('home.html', data=msg, title=t)


@app.route('/download')
def download_page():
    t = ' - Download - '
    return render_template("download.html", title=t)


@app.route('/gdn')
def gdn_page():
    t = ' - GDN - '
    return render_template("gdn.html", title=t)


if __name__ == '__main__':
    app.run(debug=True)
    CORS(app)
