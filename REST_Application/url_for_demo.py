from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/user')
def hello_admin():
    return 'Hello admin'

@app.route('/user/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest'%guest
@app.route('/user/<name>')
def login(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == '__main__':
   app.run(debug = True)

