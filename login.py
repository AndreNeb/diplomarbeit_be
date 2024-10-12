# imports
import mysql.connector, pymysql
from mysql.connector import Error
from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

# connection to database
con = mysql.connector.connect(
    host="152.89.239.166",
    port="12345",
    user="conUserData",
    password="conUserData_2024-25",
    database="DA_UserData"
)
# test connection
try:
    if con.is_connected():
        print("Connected")
except Error as e:
    print("Error: " + str(e))
cur = con.cursor()

# creating new application in flask called app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        entered_username = request.form.get("username")
        entered_password = request.form.get("password")
        query = "SELECT * FROM user_data WHERE username = %s and password = %s"
        cur.execute(query, (entered_username, entered_password))
        ans = cur.fetchall()
        print(ans)  # ['id', 'username', 'password']
        return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    global con
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        query = "INSERT INTO user_data(username, password) VALUES (%s, %s)"
        cur.execute(query, (username, password))
        con.commit()
    return render_template("sign_up.html")



if __name__ == "__main__":
    app.run()
