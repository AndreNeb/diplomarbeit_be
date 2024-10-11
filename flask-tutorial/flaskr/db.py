import mysql.connector
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['152.89.239.166'],
            port=current_app.config['12345'],
            user=current_app.config['conUserData'],
            password=current_app.config['conUserData_2024-25'],
            database=current_app.config['DA_UserData']
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
