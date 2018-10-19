from flask_restful import Api

from App.apis.goodsApi import GoodsResource
from App.apis.userApi import RegisterResource, LoginResource
from App.apis.wheelApi import WheelResource

api = Api()

def init_api(app):
    api.init_app(app)



# 添加资源
api.add_resource(WheelResource,'/api/v1/wheel/')        # 轮播图资源
api.add_resource(RegisterResource,'/api/v1/register/')  # 注册接口
api.add_resource(LoginResource,'/api/v1/login/')           # 登录验证接口
api.add_resource(GoodsResource,'/api/v1/goods/')          # 商品接口








