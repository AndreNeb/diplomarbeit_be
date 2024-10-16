import mysql.connector
from mysql.connector import Error
from flask_mysqldb import MySQL

def conDB_UserData():
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
    except Error as e: print("Error: " + str(e))
    cur = con.cursor()
    return con

def conDB_Codes():
    con = mysql.connector.connect(
        host="152.89.239.166",
        port="12345",
        user="conDA-DB",
        password="conDA-DB_2024-25",
        database="DA_LsgKatalog_Stat"
    )
    # test connection
    try:
        if con.is_connected():
            print("Connected")
    except Error as e:
        print("Error: " + str(e))
    return con

def conAutofill(app):
    app.config['MYSQL_HOST'] = '152.89.239.166'
    app.config['MYSQL_USER'] = 'DA_NeededCodes'
    app.config['MYSQL_PASSWORD'] = 'DA_NeededCodes_2024-25'
    app.config['MYSQL_DB'] = 'DA_NeededCodes'
    return MySQL(app)
