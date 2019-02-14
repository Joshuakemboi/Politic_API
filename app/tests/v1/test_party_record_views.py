from .base_test import *
import unittest
from io import BytesIO

testapp = app.test_client()

class TestParty(unittest.TestCase):
    def party(self,party_name , party_headquarters_address ,party_logo_url):
        return testapp.post('/api/v1/party',data=dict(party_name=party_name,
         party_headquarters_address = party_headquarters_address, party_logo_url = party_logo_url),follow_redirects=True )
    def test_valid_inputs(self):
        response = self.party(party_name='jubilee',party_headquarters_address = "jossgmail",party_logo_url = "lion")
        self.assertEqual(response.status_code,201)


    def put_party(self,party_name , party_headquarters_address ,party_logo_url):
        return testapp.put('/api/v1/party/1',data=dict(party_name=party_name,
         party_headquarters_address = party_headquarters_address, party_logo_url = party_logo_url),follow_redirects=True)
    def test_put_valid_inputs(self):
        response = self.put_party(party_name='jubilee',party_headquarters_address = "jos@gmail.com",party_logo_url = "lion")
        self.assertEqual(response.status_code,201)
    def test_put_taken_party_name(self):
        response = self.put_party(party_name='taken_party',party_headquarters_address = "jos@gmail.com",party_logo_url = "lion")
        self.assertEqual(response.status_code,400)
    def test_put_taken_hq_address(self):
        response = self.put_party(party_name='jubilee',party_headquarters_address = "taken_hq",party_logo_url = "lion")
        self.assertEqual(response.status_code,400)

    def party_missing_fields(self):
        return testapp.post('/api/v1/party',data=dict(),follow_redirects=True)
    def test_party_missing_fields(self):
        response = self.party_missing_fields()
        self.assertEqual(response.status_code,400)

   
    def party_edit_missing_fields(self):
        return testapp.put('/api/v1/party/1000',data=dict(),follow_redirects=True)
    def test_party_edit_missing_fields(self):
        response = self.party_edit_missing_fields()
        self.assertEqual(response.status_code,400)

   
    def get_party(self):
        return testapp.get('/api/v1/party/1000')
    def test_get_party(self):
        response = self.get_party()
        self.assertEqual(response.status_code, 200)

   
    def get_missing_party(self):
        return testapp.get('/api/v1/party/999')
    def test_get_missing_party(self):
        response = self.get_missing_party()
        self.assertEqual(response.status_code, 400)

   
    def get_parties(self):
        return testapp.get('/api/v1/party')
    def test_get_parties(self):
        response = self.get_parties()
        self.assertEqual(response.status_code, 200)

    
    def delete_party(self):
        return testapp.delete('/api/v1/party/100')
    def test_delete_party(self):
        response = self.delete_party()
        self.assertEqual(response.status_code,201)

  
    def delete_missing_party(self):
        return testapp.delete('/api/v1/party/99')
    def test_delete_missing_party(self):
        response = self.delete_missing_party()
        self.assertEqual(response.status_code,404)