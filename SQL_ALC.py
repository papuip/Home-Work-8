from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

db_name='mydb.sqlite'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer(), unique=False, nullable=True)


    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def __repr__(self):
        return f'<Student {self.name}-{self.age}>'

#db.create_all()

#Data Creator
# Add_Student=Students("Tengo","Tengo@gmail.com",29)
# db.session.add(Add_Student)
# db.session.commit()
#Selecting First Row


#student_Query=Students.query.filter_by(id=2).first() #Filtring

#print(student_Query)
#Changing All 5 Rows Below
# studen_Query=Students.query.filter_by(id=6).first()
# studen_Query.age=39
# studen_Query.name="Tengo"
# studen_Query.email="Tengiz@gmail.com"
# db.session.add(studen_Query)
# db.session.commit()

#Delete information
# studen_Query=Students.query.filter_by(id=6).first()
# db.session.delete(studen_Query)
# db.session.commit()

#quit()

#todos = {}

class StudentsX(Resource):
    def get(self, student_id):
        #return {todo_id: todos[todo_id]}
        student=Students.query.filter_by(id=student_id).first()
        print("*"*200)
        print(type(student))
        return student.name
    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}
    def post(self,name,age):
        email=f'{name}{age}@{name}.com'
        student=Students(name,email,age)
        print(student)
        db.session.add(student)
        db.session.commit()
        return f"Student {name} was added to database"

    def put(self, name, age):
        student = Students.query.filter_by(name=name).first()
        student.age = age
        db.session.add(student)
        db.session.commit()
        return f"Student {name} was modified to database"

    def delete(self, name,age):

        student=Students.query.filter_by(name=name).first()
        db.session.delete(student)
        db.session.commit()
        return f"Student {name} was deleted from database"


api.add_resource(StudentsX, '/read/<int:student_id>',endpoint="get")
api.add_resource(StudentsX, '/edit/<string:name>/<int:age>',endpoint="put")
api.add_resource(StudentsX, '/remove/<string:name>',endpoint="delete")
api.add_resource(StudentsX, '/create/<string:name>/<int:age>',endpoint="post")
#1:23:00

if __name__ == '__main__':
    app.run(debug=True)