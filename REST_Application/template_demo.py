from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello(user):
    return render_template('index.html',name=user)

if __name__=="__main__":
    app.run(debug=True)