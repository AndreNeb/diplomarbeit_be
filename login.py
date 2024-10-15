# imports
import conDatabase as db
import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash

# connection to database
con = db.conDB_UserData()
cur = con.cursor()

# creating new application in flask called app
app = Flask(__name__)

# home site
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        try:
            entered_username = request.form.get("username")
            entered_password = request.form.get("password")
            query = "SELECT username, password FROM user_data WHERE username = %s"
            cur.execute(query, entered_username)
            ans = cur.fetchall()    # ['username', 'password']
            user = str(ans[0])
            password = check_password_hash(str(ans[1]), entered_password)
            print(print)
        except Error as e:
            print("No username found!")  # ['id', 'username', 'password']
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    global con
    if request.method == "POST":
        hashed_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256')
        username = request.form.get("username")
        query = "INSERT INTO user_data(username, password) VALUES (%s, %s)"
        cur.execute(query, (username, hashed_password))
        con.commit()
    return render_template("sign_up.html")

if __name__ == "__main__":
    app.run()