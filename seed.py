from os import system
import random
from random import randrange
from datetime import timedelta, datetime
from model import connect_to_db
from server import app

system("dropdb ")
system("createdb")

connect_to_db(app)

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


d1 = datetime.strptime('12/18/2023 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/18/2024 4:50 AM', '%m/%d/%Y %I:%M %p')
print(random_date(d1, d2))