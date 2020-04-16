from flask import Flask, render_template, request, Blueprint
import time
import json
import base64
import requests
from Admin.DB import *

app_view = Blueprint('app_view', __name__)

@app_view.route('/',methods=['POST','GET'])
def index():
    # ip = request.remote_addr       #获取访问者ip
    # print(ip)
    Time = time.strftime('%Y-%m-%d')
    data = Ritui.query.filter().all()[-1]
    names = []
    min_datas = []
    max_datas = []
    Knowledge = []
    name = data.name
    zhongshu = data.study_name
    fenbu = data.put_plants
    knowledge = data.min_knowledge
    names.append(name)
    min_datas.append(zhongshu)
    max_datas.append(fenbu)
    Knowledge.append(knowledge)
    photo_data = Photo.query.filter().all()[-1]
    p = photo_data.path
    return render_template("仿.html", names=names, min_datas=min_datas, max_datas=max_datas, Time=Time, Knowledge=Knowledge, ph=p)

@app_view.route('/serch',methods=['POST','GET'])
def serch():
    return render_template("serch.html")

@app_view.route('/Serch',methods=['POST'])
def Serch():
    D = []
    N = []
    data = request.form.get('serch')
    messages = Plants.query.filter_by(name=data).first()
    N.append(messages.body)
    photo_messages = Photo.query.filter_by(name=data).first()
    D.append(photo_messages.path)
    ph = {'src': D}
    now = {"nowname": data}
    post = {'message': N}
    return render_template('model.html', title='Plants', **post,**now,**ph)

@app_view.route('/List',methods=['POST','GET'])
def serch_list():
    names = []
    datas = Plants.query.filter().all()
    for data in datas:
        name = data.name
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
    data = list_name
    messages = Plants.query.filter_by(name=data).first()
    N.append(messages.body)
    photo_messages = Photo.query.filter_by(name=data).first()
    D.append(photo_messages.path)
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

# 上传图片识别
@app_view.route('/push',methods=['POST','GET'])
def push():
    D = []
    N = []
    img = request.files.get('photo')
    img.save('../static/push/test.jpg')
    lujing = '../static/push/test.jpg'
    name = baidu_api(lujing)
    print(name)
    data = name
    messages = Plants.query.filter_by(name=data).first()
    N.append(messages.body)
    photo_messages = Photo.query.filter_by(name=data).first()
    D.append(photo_messages.path)
    ph = {'src': D}
    now = {"nowname": name}
    post = {'message': N}
    return render_template('model.html', title='Plants', **post, **now, **ph)

@app_view.route('/json_out/<name>',methods=['POST','GET'])
def json_out(name):
    N = []
    dict_json = {}
    args = name
    messages = Plants.query.filter_by(name=args).first()
    N.append(messages.body)
    dict_json['name'] = name
    dict_json['body'] = N
    return json.dumps(dict_json, ensure_ascii=False)

@app_view.route('/wx_tui',methods=['POST','GET'])
def wx_tui():
    dict_json = {}
    Time = time.strftime('%Y-%m-%d')
    data = Ritui.query.filter().all()[-1]
    names = []
    min_datas = []
    max_datas = []
    Knowledge = []
    name = data.name
    zhongshu = data.study_name
    fenbu = data.put_plants
    knowledge = data.min_knowledge
    names.append(name)
    min_datas.append(zhongshu)
    max_datas.append(fenbu)
    Knowledge.append(knowledge)
    photo_data = Photo.query.filter().all()[-1]
    dict_json['name'] = names
    dict_json['knowledge'] = Knowledge
    dict_json['photo'] = photo_data.path
    dict_json['time'] = Time
    return json.dumps(dict_json, ensure_ascii=False)

@app_view.route('/wx_photo',methods=['GET','POST'])
def wx_photo():
    Time = time.strftime('%Y%m%d'+'%H%M%S')
    path = '../static/wx_photo/'+Time+'.jpg'
    img = request.files.get('file')
    img.save(path)
    name = baidu_api(path)
    print(name)
    N = []
    dict_json = {}
    args = name
    messages = Plants.query.filter_by(name=args).first()
    N.append(messages.body)
    dict_json['name'] = name
    dict_json['body'] = N
    return json.dumps(dict_json, ensure_ascii=False)
def baidu_api(lujing):
    '''
    调用百度植物识别api进行植物识别
    '''
    lujing = lujing
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
    # 二进制方式打开图片文件
    f = open(lujing, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.492596bf4758bb09ca7de0494df007c8.2592000.1588136146.282335-19160109'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data = response.json()
        Data = data['result'][0]
        name = Data['name']
    return name
