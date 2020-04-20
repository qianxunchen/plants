from flask import Flask, render_template, request, Blueprint
from Admin.BASE import *
from Admin.DB import *
from Login.login import login_auth

app_admin = Blueprint('app_admin', __name__,)

@app_admin.route('/admin', methods=['GET','POST'])
def admin():
    passwd = request.cookies.get('passwd')
    if login_auth(passwd):
        return render_template('admin.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_up', methods=['GET', 'POST'])
def add_up():#添加
    add_name = request.form.get('add_name')
    add_text = request.form.get('add_text')
    add_photo = request.form.get('name_photo')
    Plants.plants_add(add_name,add_text)
    Photo.photo_add(add_name,add_photo)
    return render_template('admin.html')

@app_admin.route('/delete', methods=['GET','POST'])
def delete():
    passwd = request.cookies.get('passwd')
    if login_auth(passwd):
        return render_template('delete.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_shan', methods=['GET', 'POST'])
def add_shan():
    shan_name = request.form.get('shan_name')
    data = Plants.query.filter_by(name=shan_name).first()
    db.session.delete(data)
    db.session.commit()
    return render_template('delete.html')

@app_admin.route('/amend', methods=['GET', 'POST'])
def amend():#修改
    passwd = request.cookies.get('passwd')
    if login_auth(passwd):
        return render_template('amend.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_gai', methods=['GET', 'POST'])
def add_gai():#修改
    add_name = request.form.get('add_name')
    add_text = request.form.get('add_text')
    Plants.query.filter_by(name=add_name).update({'body': add_text})
    db.session.commit()
    return render_template('amend.html')

@app_admin.route('/serch_admin',methods=['POST','GET'])
def serch_admin():
    passwd = request.cookies.get('passwd')
    print(passwd)
    if login_auth(passwd):
        return render_template('serch_admin.html')
    else:
        return render_template("login.html")

# /----------------------------------发布-------------------------/

@app_admin.route('/fabu',methods=['POST','GET'])
def fabu():
    passwd = request.cookies.get('passwd')
    if login_auth(passwd):
        return render_template('fabu.html')
    else:
        return render_template("login.html")

@app_admin.route('/add_fabu',methods=['POST','GET'])
def add_fabu():
    name = request.form.get('name')
    name_study = request.form.get('name_study')
    name_put = request.form.get('name_put')
    min_know = request.form.get('min_know')
    path = request.form.get('name_photo')
    Ritui.ritui_add(name, name_study, name_put, min_know)
    Photo.photo_add(name, path)
    return "发布成功"
