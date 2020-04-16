from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,   template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cjr622622@localhost:3306/study?charset=utf8'
    db.init_app(app)
    return app,db
