from model import db, User, Date, Date_Name, Comment, connect_to_db
import datetime

def create_user(user_name, password):
    """Create and return a new user."""
    user = User(user_name=user_name, password=password)

    return user

def get_user_by_id(id):
    """Return a user by primary key."""

    return User.query.get(id)

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_user_name(user_name):
    """Return a user by user_name."""

    return User.query.filter_by(user_name = user_name).first()
    print(User.query.all())

def create_date(date, time, user_id):
    """Create and return a new date."""
    new_string = date + " " + time
    date_time = datetime.datetime.strptime(new_string, "%Y-%m-%d %H:%M")
    new_date = Date(date=date_time, user_id=user_id)


    return new_date

def add_comment(comment, date_id):
    new_comment = Comment(comment=comment, date_id=date_id)
    print(new_comment)
    return new_comment

def add_name(name, date_id):
    named = Date_Name(name=name, date_id=date_id)
    print(named)
    return named

def get_dates():
    return Date.query.all()

def get_date_by_id(id):
    return Date.query.get(id)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)