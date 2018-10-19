from flask_restful import Resource, fields,marshal_with

from App.models import Wheel


data_fields = {
    'imgPath':fields.String
}


response_fields = {
    'status':fields.Integer,
    'message':fields.String,
    'data':fields.List(fields.Nested(data_fields))
}



class WheelResource(Resource):
    @marshal_with(response_fields)
    def get(self):
        wheels = Wheel.query.all()
        response_data = {}
        response_data['status'] = 200
        response_data['message'] = '成功'
        response_data['data'] = wheels

        return response_data







