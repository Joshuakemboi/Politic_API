from .base_test import *
import unittest

testapp = app.test_client()

class TestOffice(unittest.TestCase):
    def office(self,office_type , office_name):
        return testapp.post('/api/v1/office',data=dict(office_type=office_type,
        office_name = office_name),follow_redirects=True)
    def test_office_valid_input(self):
        response = self.office(office_type='federal',office_name = "Default_office_party" )
        self.assertEqual(response.status_code,201)

    def test_taken_office_name(self):
        response = self.office(office_type='federal',office_name = "Default_office_name")
        self.assertEqual(response.status_code,201)

    def office_missing_fields(self,office_type):
        return testapp.post('/api/v1/office',data=dict(office_type=office_type),follow_redirects=True)
    def get_office(self):
        return testapp.get('/api/v1/office')

    def get_missing_office(self):
        return testapp.get('/api/v1/office')
    def test_get_missing_office(self):
        response = self.get_missing_office()
        self.assertEqual(response.status_code,200)

    def get_offices(self):
        return testapp.get('/api/v1/office')
    def test_get_office(self):
        response = self.get_office()
        self.assertEqual(response.status_code, 200)

    # def test_get_missing_office(self):
    #     response = self.get_missing_office()
    #     self.assertEqual(response.status_code, 400)

    def test_get_offices(self):
        response = self.get_offices()
        self.assertEqual(response.status_code, 200)


    def test_office_missing_fields(self):
        response = self.office_missing_fields(office_type='federal')
        self.assertEqual(response.status_code,400)