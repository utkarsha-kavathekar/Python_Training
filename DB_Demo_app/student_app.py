from flask import Flask, render_template,request
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/studentdb'
db = SQLAlchemy(app)

class Student(db.Model):

    __tablename__="student"
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))  
    marks = db.Column(db.Integer)
    
    def __init__(self, name, address, marks):
        self.name = name
        self.address = address
        self.marks = marks
        

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/add_student', methods=['POST','GET'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        name=request.form['name']
        address=request.form['address']
        marks=request.form['marks']
        print(name," ",address," ",marks)
        s1=Student(name,address,marks)
        db.session.add(s1)
        db.session.commit()
        return render_template('Success.html')

@app.route('/list_student')
def list_student():
    students=Student.query.all()
    results=[
        {
            "id":student.id ,
            "name":student.name ,
            "address":student.address ,
            "marks":student.marks
        }
        for student in students
    ]
    return render_template('list_student.html',result=results)

@app.route('/update_student/<int:id>',methods=['POST','GET'])
def update_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('update_student.html',student=student)
    else:
        student.name=request.form['name']
        student.address=request.form['address']
        student.marks=request.form['marks']
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('list_student'))

@app.route('/delete_student/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('list_student'))

if __name__ == '__main__':
   app.run(debug = True)