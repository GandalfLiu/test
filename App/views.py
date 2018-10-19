import hashlib
import uuid

from flask import Blueprint, render_template, request, session, redirect, url_for

from App.ext import db
from App.models import Wheel, User

blue = Blueprint('blue',__name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


# 首页
@blue.route('/')
@blue.route('/index/')
def index():
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
        phone = user.phone
    else:
        phone = None





    return render_template('index.html',phone=phone)


# 注册
@blue.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        password = secret_password(password)
        user = User()
        user.phone = phone
        user.password = password
        user.token = str(uuid.uuid5(uuid.uuid4(),'register'))
        db.session.add(user)
        db.session.commit()

        # 状态保持
        session['token'] = user.token
        return redirect('/index/')


# 退出登录
@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect('/index/')


# 登录操作
@blue.route("/login/",methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        password = secret_password(password)
        user = User.query.filter(User.phone == phone).first()
        # user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
        # db.session.add(user)
        # db.session.commit()
        if user.password == password:
            session['token'] = user.token
            return redirect('/index/')
        else:
            session['token'] = user.token
            return redirect('/logout/')







# ajax 验证帐号
@blue.route('/check/')
def check():
    phone = request.args.get('phone')
    print(phone,'hhhhhhhhhhh')
    users = User.query.filter(User.phone == phone)
    if  users.count()>0:
        result = '0'
    else:
        result = '1'

    return result



# 注册验证
@blue.route('/checkuser/')
def checkuser():
    phone = request.args.get('phone')
    users = User.query.filter(User.phone == phone)
    if users.count()>0:
        result = '0'   # 电话已经存在
    else:
        result = '1'    # 电话不存在
    return result




@blue.route('/1check/')
def jjcheck():
    data = request.args.get('data')
    print(data)
    return ''



# md5密码加密
def secret_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.digest()

