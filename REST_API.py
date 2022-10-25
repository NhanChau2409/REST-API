from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)

# Get path of file
basedir = os.path.abspath(os.path.dirname(__file__))

# Connect SQLAlchemy to sqlite datbase of file 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'db.sqlite')

# Innit database
db = SQLAlchemy(app)

# Database Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(20), nullable =False)
    salary = db.Column(db.Integer, nullable =False)
    
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

with app.app_context():
    db.create_all()

# Innit Marshmallow schema 
ma = Marshmallow(app)

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'salary')

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Add employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    id = request.json['id']
    name = request.json['name']
    salary = request.json['salary']
    
    new_employee = Employee(id, name, salary)
    
    db.session.add(new_employee)
    db.session.commit()
    
    return employee_schema.jsonify(new_employee)

@app.route('/employee', methods=['GET'])
def get_all_employee():
    all_employee = db.query.all()
    return jsonify(employees_schema.dump(all_employee))

@app.route('/employee/<id>', methods=['GET'])
def get_single_employee(id):
    single_employee = db.query(id)
    return employee_schema.dump(single_employee)

if __name__ == "__main__":
    app.run()