from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "asoidf080g08eg"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/dates')
def date():

    user_name = session["user_user_name"]
    user = crud.get_user_by_user_name(user_name)
    dates = crud.get_dates()
    return render_template("dates.html", user=user)

@app.route("/login", methods = ["POST"])
def login():
    user_name = request.form["user_name"]
    password = request.form["password"]

    user = crud.get_user_by_user_name(user_name)
    print(user)

    if not user or user.password != password:
        print("login failed")
        flash("The user name or password you entered was incorrect.")
    else:
        session["user_user_name"] = user.user_name
        session["user_id"] = user.id
        flash(f"Welcome back, {user.user_name}!")

    return redirect("/dates")

@app.route("/users", methods=["POST"])
def register_user():
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    user = crud.get_user_by_user_name(user_name)
    if user:
        flash("Cannot create an account with an existing user name. Try again.")
    else:
        user = crud.create_user(user_name, password)
        db.session.add(user)
        db.session.commit()
        flash("Accout created! Please log in.")

        return redirect("/")

@app.route("/users")
def all_users():
    users = crud.get_users()
    return render_template("all_users.html", users=users)

@app.route("/details", methods=["POST"])
def date_details():
    i = request.form.get("dtid")
    date = crud.get_date_by_id(i)
    session["date_id"] = date.id
    print(i)
    print(date)
    return render_template("details.html", date=date)


@app.route("/create", methods=["POST"])
def new_date():
    date = request.form.get("date")
    time = request.form.get("time")
    user_id = session["user_id"]
    # print(date, time)
    # print(type(date))
    # print(type(time))
    new_date = crud.create_date(date, time, user_id)
    # print(new_date)
    db.session.add(new_date)
    db.session.commit()

    return redirect("/dates")

@app.route("/comment", methods=["POST"])
def new_comment():
    comment = request.form.get("addc")
    print(comment)
    date = session["date_id"]

    new_comment = crud.add_comment(comment, date)
    db.session.add(new_comment)
    db.session.commit()

    return redirect("/details")

@app.route("/name", methods=["POST"])
def create_name():
    name = request.form.get("create_name")
    print(name)
    date = session["date_id"]

    n = crud.add_name(name, date)
    db.session.add(n)
    db.session.commit()

    return redirect("/details")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)