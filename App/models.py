


from App.ext import db

# 轮播图
class Wheel(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    imgPath = db.Column(db.String(100))



# 用户类
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(200))
    token = db.Column(db.String(200))


#　商品类
class Goods(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    path = db.Column(db.String(100))
    price = db.Column(db.String(20))
    detail = db.Column(db.String(100))
