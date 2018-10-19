from flask import request
from flask_restful import Resource, reqparse, marshal_with, fields

from App.models import User
from App.views import secret_password

parser = reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True,help='请输入电话号码')
# parser.add_argument('password',type=str,required=True,help='请输入密码')


response_fields = {
    'status':fields.Integer,
    'message':fields.String,
    'error':fields.String(default='')
}




# 用户注册验证api接口
class RegisterResource(Resource):
    @marshal_with(response_fields)
    def get(self):
        parse = parser.parse_args()
        phone = parse.get('phone')
        # password = parse.get('password')
        users = User.query.filter(User.phone == phone)
        response_data = {}
        if users.count()>0:     # 电话已经存在,注册不成功
            response_data['status'] = 401
            response_data['message'] = '注册失败'
            response_data['error'] = '帐号已经存在'
        else:
            response_data['status'] = 200
            response_data['message'] = '注册成功'
        return response_data



# 用户登录api验证接口
class LoginResource(Resource):
    def get(self):
        phone = request.form.get('phone')
        password = request.form.get('password')
        password = secret_password(password)

        users = User.query.filter(User.phone)
        if users.count()>0:     # 电话存在，
            user = users.first()
            if user.password == password:   # 密码正确
                return {'status':200}
            else:
                return {'status':401,'message':'密码错误'}

        else:                   # 电话不存在
            response_data = {
                'status':401,
                'message':'登录失败，账户不存在'
            }
            return response_data


