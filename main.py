from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
#app.config['SECRET_KEY'] = "AFG@#DGAFDSGSGS"


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    account_no = db.Column(db.String(100), unique=True)
    amount = db.Column(db.Integer)


db.create_all()

@app.route("/")
def index():
    return render_template("basicbanking.html")

@app.route("/details", methods=["GET", "POST"])
def details():
    if request.method == "POST":
        name_n = request.form['Name']
        account_N = request.form['Accountno']
        amount_n = request.form['Amount']
        new_book = User(name=name_n, account_no=account_N, amount=amount_n)
        db.session.add(new_book)
        db.session.commit()
    all_books = db.session.query(User).all()
    return render_template("viewcustomer.html", data=all_books)

@app.route("/add")
def add_data():
    return render_template("index.html")

@app.route("/about_bank")
def about():
    return render_template("bankabout.html")


if __name__ == "__main__":
    app.run(debug=True)