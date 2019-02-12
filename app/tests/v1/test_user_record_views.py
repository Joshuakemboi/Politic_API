from app import app
from .base_test import BaseTest
import unittest

testapp = app.test_client()

class Test_test(unittest.TestCase):
    def user(self,first_name,second_name,other_name,email,phone_number,passport_url,password,repeat_password):
        return testapp.post('/api/v1/user',data=dict(first_name=first_name,
        second_name = second_name , other_name = other_name,email=email,
        phone_number=phone_number,passport_url = passport_url ,password=password,
        repeat_password=repeat_password),follow_redirects=True)

    def user_missing_fields(self,first_name,second_name,other_name,email,password,repeat_password):
        return testapp.post('/api/v1/user',data=dict(first_name=first_name,
        second_name = second_name , other_name = other_name,email=email,
        password=password,repeat_password=repeat_password),follow_redirects=True)

    def test_user_valid_inputs(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='josh@gmail.com',phone_number='0702983637',passport_url = "passport.png",password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)

    def test_user_invalid_password(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='josh@gmail.com',phone_number='0799087221',passport_url = "passport",password='JP',
        repeat_password='JP')
        self.assertEqual(response.status_code,400)

    def test_user_registration_different_passwords(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='kim@gmail.com',phone_number='0799087221',passport_url = "passport",password='Joshu455s%',
        repeat_password='Joshu455s%')
        self.assertEqual(response.status_code,400)

    def test_user_registration_no_inputs(self):
        response = self.user(first_name='',second_name = "",other_name = "",
        email='',phone_number='',passport_url = "",password='',
        repeat_password='')
        self.assertEqual(response.status_code,400)

    def test_user_taken_email(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='taken_email@gmail.com',phone_number='+254799087221',passport_url = "passport",password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)

    def test_user_taken_phone_number(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='email@gmail.com',phone_number='+254700000000',passport_url = "passport",password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)

    def test_user_invalid_email(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='emailgmail.com',phone_number='0720000000"',passport_url = "passport",password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)

    def test_user_invalid_phone(self):
        response = self.user(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='emailgmail.com',phone_number='0700000000',passport_url = "passport",password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)

    def test_user_missing_fields(self):
        response = self.user_missing_fields(first_name='joshua',second_name = "kemboi",other_name = "rop",
        email='emailgmail.com',password='Joshu455s',
        repeat_password='Joshu455s')
        self.assertEqual(response.status_code,400)
