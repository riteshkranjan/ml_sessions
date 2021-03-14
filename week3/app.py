from flask import Flask,json, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/ml_db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        return "id is {} name is {} and age is {}".format(self.id, self.name, self.age)

@app.route('/', methods=['GET','POST'])
def welcome():
    if request.form:
        name = request.form.get("name")
        age = request.form.get("age")
        add_employee(name, age)

    ee = Employee.query.all()
    return render_template('home.html', employees=ee)

@app.route('/update', methods=['POST'])
def update_employee():
    name = request.form.get("name")
    age = request.form.get("age")
    id = request.form.get("id")
    e = Employee.query.get(id)
    e.name = name
    e.age = age
    db.session.commit()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_employee():
    id = request.form.get("id")
    e = Employee.query.get(id)
    db.session.delete(e)
    db.session.commit()
    return redirect('/')

@app.route('/add/<name>/<age>')
def add_employee(name, age):
    e = Employee(name, age)
    db.session.add(e)
    db.session.commit()
    return "data added successfully"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/ml_db'
    db.create_all()
    app.run(port = '9090')