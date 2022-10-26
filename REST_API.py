from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from marshmallow import Schema

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
    id = Column(Integer, primary_key =True)
    name = Column(String(20), nullable =False)
    salary = Column(Integer, nullable =False)
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

with app.app_context():
    db.create_all()

# Innit Marshmallow schema 
ma = Marshmallow(app)

class EmployeeSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'salary')

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Add employee
@app.route('/add_employee', methods=['POST'])
def add_employee():
    
    name = request.json['name']
    salary = request.json['salary']
    
    new_employee = Employee(name, salary)
    
    db.session.add(new_employee)
    db.session.commit()
    
    return jsonify(employee_schema.dump(new_employee))

@app.route('/employee', methods=['GET']) 
def get_all_employee():
    all_employee = Employee.query.all()
    return jsonify(employees_schema.dump(all_employee))

@app.route('/employee/<id>', methods=['GET'])
def get_single_employee(id):
    single_employee = Employee.query.get(id)
    return jsonify(employee_schema.dump(single_employee))

@app.route('/employee/update/<id>', methods=['PUT'])
def get_update_employee(id):
    update_employee = Employee.query.get(id)
    
    name = request.json['name']
    salary = request.json['salary']
    
    update_employee.name = name
    update_employee.salary = salary
    
    db.session.commit()
    
    return jsonify(employee_schema.dump(update_employee))

@app.route('/employee/delete/<id>', methods=['DELETE'])
def get_delete_employee(id):
    delete_employee = Employee.query.get(id)
    
    db.session.delete(delete_employee)
    db.session.commit()
    
    return jsonify(employee_schema.dump(delete_employee))


if __name__ == "__main__":
    app.run()