import re
from ..models.office_record_models import OfficeRecord , all_offices
from flask_restful import Resource , reqparse , Api,abort
from app import app, api

office_parser = reqparse.RequestParser()
office_parser.add_argument('office_type', type=str, help='Enter office type', required=True)
office_parser.add_argument('office_name', type=str, help='Enter office type', required=True)

class Office(Resource):
    def get(self):
        offices = OfficeRecord()
        return {"data":offices.get_all_offices()},200

    def post(self):
        office_args = office_parser.parse_args()
        office_type =office_args['office_type']
        office_name =office_args['office_name']
        if not office_type or not office_name:
            return {"message":"All the fields must be filled"}
        office = OfficeRecord()
        office = office.create_office(office_type , office_name)
        return office, 201


class SingleOffice(Resource):
    def get(self,office_id):
        single_office = OfficeRecord()
        return single_office.get_single_office(office_id)



api.add_resource(SingleOffice, '/api/v1/office/<int:office_id>')
api.add_resource(Office, '/api/v1/office')
