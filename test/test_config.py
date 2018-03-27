from app import admin-login
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
#        pass
#    self.app = creat_app('testing')
#    self.client = self.app.test_client
#    self.user_date = {
#        
#        'username':'Piere',
#        'email': 'piere@test.com',
#        'password': 'saltadmin',
#        
#    }
#    self.app_context = self.app.app_context()
#    self.app_context.push()
#        
#    def test_user_registration(self):
#    	#Test api can register user
#    	result = self.client().post('/api/auth/register', data=self.user_data)
#    	self.assertEqual(result.status_code, 201)
#
#
#    def test_user_login(self):
#    	#test api allows user to login
#    	self.test_user_registration()
#    	result=self.client().post('/auth/login', data=dict(
#    		email='john@mail.com',
#    		password='John2018'
#    		), follow_redirects=True)
#    	self.assertIn(b'You are now logged in', result.data)
#
#
#    def test_user_logout(self):
#    	#test api allows user to logout
#    	#register and login first
#    	self.test_user_login
#    	#follow redirect to logout and message displayed
#    	res = self.client().get('/auth/logout', follow_redirects=True)
#    	self.assertIn(b'You were logged out', res.data)
#
#
#
#    def test_user_password_reset(self):
#    	#test api allows user to reset their password /api/auth/reset-password
#    	self.test_user_login()
#    	reset_result = self.client().post('/auth/reset-password', data={
#    		'email':'john@mail.com',
#    		'old_password':'John2018',
#    		'new_password':'Change123'
#    	})
#    	login_result = self.client().post('/auth/login', data={
#    		'email':'john@mail.com',
#    		'password':'Change123'
#    	})
#    	self.assertEqual(login_result.status_code, 200)
#
#
#    def tearDown(self):
#    	#Teardown Initialized variables
#    	self.app_context.pop()

    if __name__ == '__main__':
        unittest.main()