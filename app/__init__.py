from  flask import Flask,jsonify
from flask_restful import  Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'Joshu455s*'

from app.API.v1.views.user_record_views import *
from app.API.v1.views.office_record_views import *
from app.API.v1.views.party_record_views import *

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return make_response(jsonify({"Data":"Not found"}),404)

@app.errorhandler(500)
def something_is_wrong(e):
    
    return make_response(jsonify({"Data":"something went wrong"}),500)