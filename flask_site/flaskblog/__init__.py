#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Q5Q3s+bE%hJolc4%EVFiA0W60h5d3&Uj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
