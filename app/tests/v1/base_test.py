import unittest
from app import app

class BaseTest(unittest.TestCase):
  """
    Base Test Class
  """

  def setUp(self):
    """
      Setup method
    """
    self.app = app
    self.client = self.app.test_client()

  def tearDown(self):
    """
      Teardown method to run after all each test
    """
    self.app = None
