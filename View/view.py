from flask import Flask, render_template, request, Blueprint
import MySQLdb
import time

app_view = Blueprint('app_view', __name__)

@app_view.route('/',methods=['POST','GET'])
def index():
    # ip = request.remote_addr
    # print(ip)
    Time = time.strftime('%Y-%m-%d')
    con = MySQLdb.connect(host='localhost', user='root', passwd='cjr622622', db='study', charset='utf8')
    con = con.cursor()
    sql = "select * from ritui order by id desc limit 1"#最新的，倒序输出
    con.execute(sql)
    results = con.fetchone()
    names = []
    min_datas = []
    max_datas = []
    Knowledge = []
    name = results[1]
    zhongshu = results[2]
    fenbu = results[3]
    knowledge = results[4]
    names.append(name)
    min_datas.append(zhongshu)
    max_datas.append(fenbu)
    Knowledge.append(knowledge)

    photo_sql = "select * from photo order by id desc limit 1"
    con.execute(photo_sql)
    p = con.fetchone()[2]
    return render_template("仿.html", names=names, min_datas=min_datas, max_datas=max_datas, Time=Time, Knowledge=Knowledge, ph=p)

@app_view.route('/serch',methods=['POST','GET'])
def serch():
    return render_template("serch.html")

@app_view.route('/Serch',methods=['POST'])
def Serch():
    D = []
    N = []
    data = request.form.get('serch')
    value = data
    con = MySQLdb.connect(host='localhost', user='root', passwd='cjr622622', db='study', charset='utf8')
    con = con.cursor()
    sql = "select * from plants where name like '%s%%'" % value
    con.execute(sql)
    numrows = int(con.rowcount)
    for i in range(numrows):
        row = con.fetchone()
        N.append(row[2])

    photo = "select * from photo where name like '%s%%'" % value
    con.execute(photo)
    numrow = int(con.rowcount)
    for x in range(numrow):
        photos = con.fetchone()
        D.append(photos[2])

    ph = {'src': D}
    now = {"nowname": data}
    post = {'message': N}
    return render_template('model.html', title='Plants', **post,**now,**ph)

@app_view.route('/List',methods=['POST','GET'])
def serch_list():
    con = MySQLdb.connect(host='localhost', user='root', passwd='cjr622622', db='study', charset='utf8')
    con = con.cursor()
    sql = "select * from plant_name"
    con.execute(sql)
    results = con.fetchall()
    names = []
    for result in results:
        name = result[1]
        names.append(name)
    return render_template('list.html',names=names)


@app_view.route('/list_serch', methods=['GET'])
def list_serch():
    global list_name
    list_name = request.args.get('name')
    print(list_name)
    # return render_template('test.html')
    return "success"

@app_view.route('/l_serch', methods=['GET'])
def l_serch():
    D = []
    N = []
    value = list_name
    con = MySQLdb.connect(host='localhost', user='root', passwd='cjr622622', db='study', charset='utf8')
    con = con.cursor()
    sql = "select * from plants where name like '%s%%'" % value
    con.execute(sql)
    numrows = int(con.rowcount)
    for i in range(numrows):
        row = con.fetchone()
        N.append(row[2])

    photo = "select * from photo where name like '%s%%'" % value
    con.execute(photo)
    numrow = int(con.rowcount)
    for x in range(numrow):
        photos = con.fetchone()
        D.append(photos[2])

    ph = {'src': D}
    now = {"nowname": list_name}
    post = {'message': N}
    return render_template('model.html', title='Plants', **post, **now, **ph)


@app_view.route('/gongzhao',methods=['POST','GET'])
def gongzhao():
    return render_template('微信公众号.html')

@app_view.route('/photo',methods=['POST','GET'])
def push_photo():
    return render_template('上传图片.html')

@app_view.route('/push',methods=['POST','GET'])
def push():
    img = request.files.get('photo')
    img.save('static/push/test.jpg')
    return "success"
