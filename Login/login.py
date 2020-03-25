from flask import Flask, render_template, request, make_response, Blueprint
import MySQLdb

app_login = Blueprint('app_login', __name__)

@app_login.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app_login.route('/login_a', methods=['POST'])
def login_a():
    Username = request.values.get('name')
    Passwd = request.values.get('passwd')
    if(Username != "admin"):
        return "用户名错误"
    elif(Passwd != "111"):
        return "密码错误"
    elif(Username =="admin" and Passwd == "111"):
        resp = make_response(render_template("admin.html"))
        '''
            设置cookie,默认有效期是临时cookie,浏览器关闭就失效
            可以通过 max_age 设置有效期， 单位是秒
        '''''
        resp.set_cookie("passwd", "123")
        return resp

#退出函数
@app_login.route('/login_out', methods=['GET','POST'])
def login_out():
    resp = make_response(render_template('login.html'))
    resp.delete_cookie('passwd')
    return resp
