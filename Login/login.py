from flask import Flask, render_template, request, make_response, Blueprint
from Admin.DB import *
import hashlib

app_login = Blueprint('app_login', __name__)
app,db = create_app()

global cookies
cookies = []

@app_login.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app_login.route('/login_a', methods=['POST'])
def login_a():
    name = request.values.get('name')
    passwd = request.values.get('passwd')
    password = md(passwd)
    data = User.query.filter_by(name=name,password=password).first()
    if(data):
        resp = make_response(render_template("admin.html"))
        '''
            设置cookie,默认有效期是临时cookie,浏览器关闭就失效
            可以通过 max_age 设置有效期， 单位是秒
        '''''
        cookie = password
        cookies.append(cookie)
        resp.set_cookie("passwd", cookie)
        return resp,cookie
    else:
        return "账号或者密码错误！"

#退出函数
@app_login.route('/login_out', methods=['GET','POST'])
def login_out():
    resp = make_response(render_template('login.html'))
    resp.delete_cookie('passwd')
    return resp


def md(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    pass_md =md5.hexdigest()
    # pass_md = str(pass_md)
    return pass_md

def login_auth(cookie):
    if(cookie in cookies):
        return True
    else:
        return False

