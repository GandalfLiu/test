from flask_restful import Resource, fields,marshal_with

from App.models import Goods


data_fields = {
    'path':fields.String,
    'price':fields.String,
    'detail':fields.String

}

response_fields = {
    'status':fields.Integer,
    'message':fields.String,
    'data':fields.List(fields.Nested(data_fields))
}

class GoodsResource(Resource):
    @marshal_with(response_fields)
    def get(self):
        goods = Goods.query.all()
        response_data = {}
        response_data['status'] = 200
        response_data['message'] = '成功'
        response_data['data'] = goods
        return response_data
