# --- imports --- #
import bcrypt
from flask import Flask, request, jsonify, redirect, url_for, render_template, session as flask_session
from flask_cors import CORS
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# --- Create new class --- #
app = Flask(__name__)
CORS(app)   # enables CORS for all routes to transfer token
app.config['SECRET_KEY'] = 'DA_Narko-Register-Login'

# --- Create connection to Database --- #
host = '152.89.239.166'
port = 12345
user = 'conUserData'
passwd = 'conUserData_2024-25'
database = 'DA_UserData'
engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}')

# --- Create Session --- #
SessionFactory = sessionmaker(bind=engine)
db_session = scoped_session(SessionFactory)
Base = declarative_base()  # creates base class for declarative class definition
Base.metadata.reflect(engine)

# --- Class User --- #
class User(Base):
    __tablename__ = Base.metadata.tables['user_data']
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user_email = data['user']  # either username or email
        password = data['password'].encode('utf-8')

        query = db_session.query(User).filter((User.user == user_email) | (User.email == user_email)).first()
        if query and bcrypt.checkpw(password, query.password.encode('utf-8')):
            flask_session['user'] = query.user  # Store the username in session
            return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'message': 'Invalid credentials or password'}), 401

@app.route('/register', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    try:
        if request.method == 'POST':
            user = data['user']
            email = data['email']
            passwd = data['password'].encode('utf-8')
            # ---  Hash password --- #
            pw_hashed = bcrypt.hashpw(passwd, bcrypt.gensalt()).decode('utf-8')
            newUser = User(user=user, password=pw_hashed, email=email)
            db_session.add(newUser)
            db_session.commit()
            return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db_session.rollback()
        return jsonify({'message': str(e)}), 400
    finally:
        db_session.remove()  # deleting session in the end

if __name__ == '__main__':
    app.run(debug=True)
