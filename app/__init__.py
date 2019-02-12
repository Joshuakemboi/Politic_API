from  flask import Flask,jsonify
from flask_restful import  Api
errors ={
    'servererror': {
        'message': "internal server error",
        'status': 500,
    }
}
app = Flask(__name__)
api = Api(app, errors=errors)
app = Flask(__name__)
api = Api(app, catch_all_404s=True)


app.config['SECRET_KEY'] = 'Joshu455s*'

from app.API.v1.views.user_record_views import *
from app.API.v1.views.office_record_views import *
from app.API.v1.views.party_record_views import *
