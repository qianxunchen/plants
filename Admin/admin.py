from flask import Flask, render_template, request, Blueprint
import MySQLdb
import time

app_admin = Blueprint('app_admin', __name__,)

@app_admin.route('/admin', methods=['GET','POST'])
def admin():
    passwd = request.cookies.get('passwd')
    if passwd == '123':
        return render_template('admin.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_up', methods=['GET', 'POST'])
def add_up():#添加
    add_id = request.form.get('add_id')
    add_name = request.form.get('add_name')
    add_text = request.form.get('add_text')
    print(add_id)
    print(add_name)
    print(add_text)
    return render_template('admin.html')

@app_admin.route('/delete', methods=['GET','POST'])
def delete():
    passwd = request.cookies.get('passwd')
    if passwd == '123':
        return render_template('delete.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_shan', methods=['GET', 'POST'])
def add_shan():
    shan_id = request.form.get('shan_id')
    shan_name = request.form.get('shan_name')
    print(shan_id)
    print(shan_name)
    return "删除成功"

@app_admin.route('/amend', methods=['GET', 'POST'])
def amend():#修改
    passwd = request.cookies.get('passwd')
    if passwd == '123':
        return render_template('amend.html')
    else:
        return render_template('login.html')

@app_admin.route('/add_gai', methods=['GET', 'POST'])
def add_gai():#修改
    add_id = request.form.get('add_id')
    add_name = request.form.get('add_name')
    add_text = request.form.get('add_text')
    print(add_id)
    print(add_name)
    print(add_text)
    return render_template('amend.html')

@app_admin.route('/serch_admin',methods=['POST','GET'])
def serch_admin():
    passwd = request.cookies.get('passwd')
    if passwd == '123':
        return render_template('serch_admin.html')
    else:
        return render_template("login.html")

# /----------------------------------发布-------------------------/

@app_admin.route('/fabu',methods=['POST','GET'])
def fabu():
    passwd = request.cookies.get('passwd')
    if passwd == '123':
        return render_template('fabu.html')
    else:
        return render_template("login.html")

@app_admin.route('/add_fabu',methods=['POST','GET'])
def add_fabu():
    name_id = request.form.get('name_id')
    name = request.form.get('name')
    name_study = request.form.get('name_study')
    name_put = request.form.get('name_put')
    min_know = request.form.get('min_know')
    name_photo = request.form.get('name_photo')
    print(name)
    print(name_id)
    print(name_study)
    print(name_put)
    print(min_know)
    print(name_photo)
    # 以下为添加到数据库代码，暂时注释掉
    con = MySQLdb.connect(host='localhost', user='root', passwd='cjr622622', db='study', charset='utf8')
    cur = con.cursor()
    sql = "insert into ritui values( %s,'%s','%s','%s','%s');" % (name_id, name, name_study, name_put, min_know)
    cur.execute(sql)
    con.commit()
    sql_photo = "insert into photo values( %s,'%s','%s');" % (name_id, name, name_photo)
    cur.execute(sql_photo)
    con.commit()
    con.close()
    return 'success'