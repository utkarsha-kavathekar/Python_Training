from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/result')
def result():
    dict={'math':90,'phy':'70','chem':80}
    return render_template('result.html',result = dict)

if __name__ == '__main__':
   app.run(debug = True)