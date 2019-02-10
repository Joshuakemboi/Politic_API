from ..models.party_record_models import PartyRecord , all_parties
from flask_restful import Resource , reqparse,Api
from app import app, api
import re
import werkzeug
from werkzeug.utils import secure_filename
import os

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/upload_logo/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

party_parser = reqparse.RequestParser()
party_parser.add_argument('party_logo', type=werkzeug.datastructures.FileStorage, location='files',required=True)
party_parser.add_argument('party_name', type=str, help='Enter party name', required=True)
party_parser.add_argument('party_headquarters_address', type=str, help='Repeat headquarters address' , required=True)

edit_party_parser = reqparse.RequestParser()
edit_party_parser.add_argument('party_logo' , type=werkzeug.datastructures.FileStorage, location='files',required=True)
edit_party_parser.add_argument('party_name', type=str, help='Enter party name', required=True)
edit_party_parser.add_argument('party_headquarters_address', type=str, help='Repeat headquarters address' , required=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Party(Resource):
    def get(self):
        registered_parties = PartyRecord()
        return registered_parties.get_all_parties()

    def post(self):
        party_args = party_parser.parse_args()
        party_name =party_args['party_name']
        party_headquarters_address =party_args['party_headquarters_address']
        party_logo =party_args['party_logo']
        if party_logo :
            party_logo_url = secure_filename(party_logo.filename)
            party_logo.save(os.path.join(app.config['UPLOAD_FOLDER'], party_logo_url))
        new_party = PartyRecord()
        parties = new_party.all_parties
        for party in parties:
            if party_name in party.values() or party_headquarters_address in party.values():
                return{"message":"Another party with similar credentials exist"},400
        party = new_party.create_party(party_name,party_headquarters_address ,party_logo_url)
        return party, 201




class SingleParty(Resource):
    def get(self , party_id):
        single_party = PartyRecord()
        if not single_party.get_single_party(party_id):
            return {"mesage":"The page you requested is currently not availlable"},400
        return single_party.get_single_party(party_id),201


    def put(self, party_id):
        edit_party_args = edit_party_parser.parse_args()
        party_name =edit_party_args['party_name']
        party_headquarters_address =edit_party_args['party_headquarters_address']
        party_logo = edit_party_args['party_logo']
        if party_logo :
            party_logo_url = secure_filename(party_logo.filename)
            party_logo.save(os.path.join(app.config['UPLOAD_FOLDER'], party_logo_url))
        new_party = PartyRecord()
        parties = new_party.all_parties
        for party in parties:
            if party_name in party.values() or party_headquarters_address in party.values():
                return{"message":"Anothe rparty with similar credentials exist"},400
        update = new_party.update_party(party_id , party_name , party_headquarters_address , party_logo_url)
        return {"message":"success"}, 201


    def delete(self , party_id):
        single_party = PartyRecord()
        if not single_party.delete_single_party(party_id):
            return {"mesage":"The page you requested is currently not availlable"},400
        single_party.delete_single_party(party_id)
        return single_party.get_all_parties(),201


api.add_resource(SingleParty, '/party/<int:party_id>')
api.add_resource(Party, '/party')