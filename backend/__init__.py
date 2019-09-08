from flask import Flask, render_template, g, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import pymysql

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/backend/static")
# 防止跨域攻击
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:12345678@database-2.cnq0sgzuhxxq.ap-southeast-2.rds.amazonaws.com:3306/b16'

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
from . import model

CORS(app)
from . import main

# 注册蓝图
app.register_blueprint(main.main)
app.config['SECRET_KEY'] = '32fa828ba'
app.debug = True


def creat_app():
    return app
