import unittest
from unittest.mock import patch
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_index_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Osteoporosis Education Chatbot', result.data)

    @patch('app.openai.ChatCompletion.create')
    def test_generate_route(self, mock_openai):
        mock_openai.return_value.choices = [type('', (), {'message': type('', (), {'content': "Mocked response"})})()]

        response = self.app.post('/generate', data=dict(prompt="Hello"))
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Mocked response', response.json['content'])
        mock_openai.assert_called_once()

if __name__ == '__main__':
    unittest.main()