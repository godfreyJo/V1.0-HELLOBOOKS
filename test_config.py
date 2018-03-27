from . import app
import unittest
import os

from flask import json 
import json

class TestConfig(unittest.TestCase):
    #functions for test cases
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/test')
        self.asserEqual(respose.status_code, 200)
#      
    if __name__ == '__main__':
        unittest.main()