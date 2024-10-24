# imports
import bcrypt
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# --- Database connection --- #
host='152.89.239.166'
port=12345
user='conUserData'
passwd='conUserData_2024-25'
database='DA_UserData'

# --- create new Class --- #
app = Flask(__name__)
CORS(app)   # enable CORS for all routes

app.config['SECRET_KEY'] = 'DA-Narko'

# --- Create engine --- # uses database connection configuration to connect to and communicate with underlying database
engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}")

# --- Configurate Session --- #
SessionFactory = sessionmaker(bind=engine)  # create db_session
session = scoped_session(SessionFactory)    #

# --- Base for the ORM-Modell --- # Object-Relational-Mapping
Base = declarative_base()   # creates base class for declarative class definitions
Base.metadata.reflect(engine)

# --- Define User-Modell --- #
class User(Base):
    __tablename__ = Base.metadata.tables['user_data']

    # defining already existing columns / table for class User
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

"""
users = db_session.query(User).all()
for i in users:
    print(i.username, i.password)
"""

# Route creating account (user, password)
@app.route('/register', methods=['POST'])
def register():     # add user
    data = request.get_json()   # analyse given JSON-data in Flask-Web-Applications from request body
    try:
        passwd = data['password'].encode('utf-8')
        passwd_hashed = bcrypt.hashpw(passwd, bcrypt.gensalt()).decode('utf-8')
        # creating new user --> nuser
        nuser = User(username=data['username'], password=passwd_hashed) # creating new user
        session.add(nuser)  # add user
        session.commit()    # commit user to database
        return jsonify({'message': 'User successfully added!'}), 201    # 201 is http status code; indicates everything was successful
    except Exception as e:
        session.rollback()
        print(f'Error: {str(e)}')
        return jsonify({'message': 'An error ocurred while adding the user'}), 400
    finally:
        session.remove()    # deleting db_session in the end

if __name__ == '__main__':
    app.run(debug=True)