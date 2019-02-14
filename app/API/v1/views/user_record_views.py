from ..models.user_record_models import UserRecord , all_users
#from datetime import datetime
from flask import Flask,flash, request, redirect, url_for
from flask_restful import Resource , reqparse,Api
from app import app, api
import re
import werkzeug
from werkzeug.utils import secure_filename
import os

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

user_parser = reqparse.RequestParser()
user_parser.add_argument('first_name', type=str, help='Enter your first name', required=True)
user_parser.add_argument('second_name', type=str, help='Enter your second name', required=True)
user_parser.add_argument('other_name', type=str, help='Enter your other name')
user_parser.add_argument('email', type=str, help='Enter your email', required=True)
user_parser.add_argument('phone_number', type=str, help='Enter your phone_number', required=True)
user_parser.add_argument('passport', type=werkzeug.datastructures.FileStorage, location='files',required=True)
user_parser.add_argument('password', type=str, help='Enter your passport_number', required=True)
user_parser.add_argument('repeat_password', type=str, help='Repeat your password' , required=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class SignupUser(Resource):
    def get(self):
        registered_users = UserRecord()
        return registered_users.get_all_users()

    def post(self):
        user_args = user_parser.parse_args()
        first_name =user_args['first_name']
        second_name =user_args['second_name']
        other_name =user_args['other_name']
        email = user_args['email']
        phone_number = user_args['phone_number']
        passport = user_args['passport']
        password = user_args['password']
        repeat_password = user_args['repeat_password']
        valid_password= re.match('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])',password)
        valid_email= re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9]+\.[a-z]+$)",email)
        if passport :
            passport_url = secure_filename(passport.filename)
            passport.save(os.path.join(app.config['UPLOAD_FOLDER'], passport_url))
        if not first_name or not second_name or not passport or not email or not phone_number  or not password or not repeat_password:
            return {"message":"Please fill all the fields"},400
        for user in all_users:
            if  phone_number in user.values():
                return {"message":"The phone number you have provided is used by another person"},400
            if  email in user.values():
                return {"message":"The email address you have provided is used by another person"},400
        if not valid_password:
            return {"message":"Please make sure that your password contains atleast one upper case letter, one lower case ,a digit and atleast one character from %$& and #"},400
        if not valid_email:
            return {"message":"Please provide a valid email address"},400
        if not phone_number.startswith('07'):
            return {"message":"A phone number should start with 07"},400
        if  repeat_password != password:
            return {"message":"The passwords you have provided don't match"},400
        user = UserRecord()
        user = user.create_user(first_name ,second_name,other_name, email , phone_number,passport_url, password , repeat_password)
        return user, 201

api.add_resource(SignupUser, '/api/v1/user')
