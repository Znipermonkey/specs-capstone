import os
import random
from random import randrange
from datetime import timedelta, datetime
import model
import server
from server import app
import crud

os.system("dropdb dates")
os.system("createdb dates")

model.connect_to_db(app)

with  app.app_context():
    model.db.create_all()

    new_user = crud.create_user("a", "a")
    model.db.session.add(new_user)
    model.db.session.commit()

    for n in range(10):
        user_name = f"user{n}"
        password = "test"

        new_user = crud.create_user(user_name, password)
        model.db.session.add(new_user)

    model.db.session.commit()

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime('12/18/2023 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/18/2024 4:50 AM', '%m/%d/%Y %I:%M %p')
print(random_date(d1, d2))