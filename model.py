
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(99), unique=True)
    password = db.Column(db.String(199))
    


    def __repr__(self):
        return f"<User user_id={self.id} user_name={self.user_name}>"
    
class Date(db.Model):
    __tablename__ = "dates"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    user = db.relationship("User", backref="dates")

    def __repr__(self):
        return f"<Date id={self.id} date={self.date}>"
    

    
    
class Date_Name(db.Model):
    __tablename__ = "date_name"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    date_id = db.Column(db.Integer, db.ForeignKey("dates.id"), nullable = False)

    names = db.relationship("Date", backref="date_name")
    def __repr__(self):
        return f"<Name id={self.id}, name={self.name}>"

class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    comment = db.Column(db.String)
    date_id = db.Column(db.Integer, db.ForeignKey("dates.id"), nullable=False)
    
    comments = db.relationship("Date", backref="comment")
    def __repr__(self):
        return f"<Comment id={self.id} comment={self.comment}>"

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)