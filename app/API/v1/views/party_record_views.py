from ..models.party_record_models import PartyRecord , all_parties
from flask_restful import Resource , reqparse,Api
from app import app, api
import re
import werkzeug
from werkzeug.utils import secure_filename
import os

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/upload_logo/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# party_parser = reqparse.RequestParser()
# party_parser.add_argument('party_logo', type=werkzeug.datastructures.FileStorage, location='files',required=True)
# party_parser.add_argument('party_name', type=str, help='Enter party name', required=True)
# party_parser.add_argument('party_headquarters_address', type=str, help='Repeat headquarters address' , required=True)

party_parser = reqparse.RequestParser()
party_parser.add_argument('party_logo_url', type=str, help='Enter party logo', required=True)
party_parser.add_argument('party_name', type=str, help='Enter party name', required=True)
party_parser.add_argument('party_headquarters_address', type=str, help='Repeat headquarters address' , required=True)

class Party(Resource):
    
    def get(self):
      
        registered_parties = PartyRecord()
        return {"Data":registered_parties.get_all_parties()},200

    def post(self):
     
        party_args = party_parser.parse_args()
        party_name =party_args['party_name']
        party_headquarters_address =party_args['party_headquarters_address']
        party_logo_url =party_args['party_logo_url']
        new_party = PartyRecord()
        parties = new_party.all_parties
        if  not party_name.isalpha():
            return{"Status":400,"message":"invalid partyname"},400
        if  not party_logo_url.isalpha():
            return{"Status":400,"message":"invalid party logo url"},400 
        if  not party_headquarters_address.isalpha():
            return{"Status":400,"message":"invalid party haedquarters url"},400   
        for party in parties:
            if party_name in party.values() or party_headquarters_address in party.values():
                return{"Status":400,"message":"Another party with similar credentials exist"},400
        
        party = new_party.create_party(party_name,party_headquarters_address ,party_logo_url)
        return {"status":201,"message":"The party was successfully created"}, 201

    


class SingleParty(Resource):
 
    def get(self , party_id):
        single_party = PartyRecord()
        if not single_party.get_single_party(party_id):
            return {"Status":400 , "Mesage":"The page you requested is currently not availlable"},400
        return {"Status":200 , "data":single_party.get_single_party(party_id)},200

    def put(self, party_id):
        
        edit_party_args = party_parser.parse_args()
        party_name =edit_party_args['party_name']
        party_headquarters_address =edit_party_args['party_headquarters_address']
        party_logo_url = edit_party_args['party_logo_url']
        new_party = PartyRecord()
        parties = new_party.all_parties
        if  not party_name.isalpha():
            return{"Status":400,"message":"invalid partyname"},400
        if  not party_logo_url.isalpha():
            return{"Status":400,"message":"invalid party logo url"},400
        for party in parties:
            if party_name in party.values() or party_headquarters_address in party.values():
                return{"Status":400,"message":"Another party with similar credentials exist"},400
       
        update = new_party.update_party(party_id , party_name , party_headquarters_address , party_logo_url)
        return {"Status":201 ,"message":"success"}, 201

    def delete(self , party_id): 
        single_party = PartyRecord()
        if not single_party.delete_single_party(party_id):
            return {"Status":404 , "mesage":"The page you requested is currently not availlable"},404
        single_party.delete_single_party(party_id)
        return {"Status":201 , "data":single_party.get_all_parties()},201


api.add_resource(SingleParty, '/api/v1/party/<int:party_id>')
api.add_resource(Party, '/api/v1/party')