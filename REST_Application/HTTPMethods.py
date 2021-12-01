from flask import Flask,request
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

app=Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s'%name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('name')
        return redirect(url_for('success',name=user))
        
@app.route('/')
def home():
    return render_template('HTTPMethodsHtml.html')

if __name__=='__main__':
    app.run(debug=True)