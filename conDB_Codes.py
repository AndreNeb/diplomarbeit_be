# imports
import mysql.connector
from mysql.connector import Error

# globals
global con, cur
tasks = ("all", "first", "last", "specific", "search")

# create connection to database
def conDatabase():
    global con, cur
    con = mysql.connector.connect(
        host="152.89.239.166",
        port="12345",
        user="conDA-DB",
        password="conDA-DB_2024-25",
        database="DA_LsgKatalog_Stat"
    )
    cur = con.cursor()
    # test connection
    try:
        if con.is_connected():
            print("Connected")
    except Error as e:
        print("Error: " + str(e))

def searchKap(task):
    if task == "all":
        query = "SELECT * FROM `Kapitel`"   # select all data from kapitel
        cur.execute(query)
        ans = cur.fetchall()    # select all items from table
        for r in ans:
            print(r)
    elif task == "first":
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[0] # select first item from table
        print(ans)
    elif task == "last":
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[-1]    # select last item from table
        print(ans)
    elif type(task) == int: # means specific number (1., 2., ...)
        num = int(task)
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[num-1]
        print(ans)
    else:   # search for contained term in complete table
        terms = str(task)
        query = "SELECT * FROM Kapitel WHERE kap_name LIKE %s"
        cur.execute(query, ('%' + terms + '%',))    # terms is bevor or after
        ans = cur.fetchall()
        for r in ans:
            print(r)

def searchReg(task):
    if task == "all":   # get all items contained in table
        query = "SELECT * FROM `Region`"
        cur.execute(query)
        ans = cur.fetchall()
        for r in ans:
            print(r)
    if type(task) == int:   # search for all regions of this chapter
        num = str(task)
        query = "SELECT * FROM `Region` WHERE kap_id LIKE %s"
        cur.execute(query, (num,))  # items only contains 1, not 10, 11, ...
        ans = cur.fetchall()
        for i in ans:
            print(i)
    else:   # means task is a string
        if task.split(".")[0] == "":    # ['', '01']; .XX
            reg = str(task)
            query = "SELECT * FROM `Region` WHERE reg_id LIKE %s"
            cur.execute(query, ('%' + reg + '%',))
            ans = cur.fetchall()
            for r in ans:
                print(r)
        else:   # search for specific region; only one possible; "01.01"
            reg = str(task)
            kap = int(task.split(".")[0])
            query = "SELECT * FROM `Region` WHERE kap_id = %s AND reg_id = %s"
            cur.execute(query, (kap, reg))
            ans = cur.fetchall()
            for r in ans:
                print(r)


