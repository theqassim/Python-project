from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '2f7e988d875d0399f12241ae9237c486860f56a35ed182c2a8f9e2fa6f5ab90e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from Project_Package import routes