from django.test import TestCase
import sys
import json
import unittest

# def output(response_type, message, download_link):
#     if download_link == '':
#        response = [
#         {
#              'type': response_type,
#              'message': message
#          }
#      ]
#      else:
#      response = [
#       {
#               'type': response_type,
#               'message': message,
#               'download_link': download_link
#        }
#      ]
#      return jsonify({'response': response})

class TestFunctions(unittest.TestCase):
 '''Test case for the client methods.'''
    def setup(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        # Test of Output function
        
        def test_output(self):
            with app.test_request_context():
            # mock object
            out = output('error', 'Test Error', 'local_host')
            # Passing the mock object
            response = [
              {
                     'type': 'error',
                     'message': 'Test Error',
                     'download_link': 'local_host'
               }
            ]
            data = json.loads(out.get_data(as_text=True)
            # Assert response
            self.assertEqual(data['response'], response)

if __name__ == '__main__':
      unittest.main()