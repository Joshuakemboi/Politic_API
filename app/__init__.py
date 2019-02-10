from  flask import Flask
from flask_restful import  Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'Joshu455s*'

from app.API.v1.views.user_record_views import *
from app.API.v1.views.office_record_views import *
from app.API.v1.views.party_record_views import *