from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World of Flask'

@app.route('/hello')
def hello():
   return 'hello world'

@app.route('/dynamic-url/<value>')
def dynamic_url(value):
    return 'Hello dynamic text in url is %s'%value

@app.route('/empid/<int:id>')
def show_id(id):
    return 'Employee id is %d'%id

@app.route('/empsalary/<float:salary>')
def show_salary(salary):
    return 'Employee salary is %f'%salary

if __name__ == '__main__':
   app.run(debug = True)