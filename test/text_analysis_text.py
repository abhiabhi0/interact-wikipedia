import unittest
import json
from api import app

class TestWordFrequencyAnalysisAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_word_frequency_analysis_success(self):
        response = self.app.get('/v1/word-frequency-analysis?topic=Python&n=5')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('top_words' in data)
        self.assertEqual(len(data['top_words']), 5)

    def test_word_frequency_analysis_page_not_found(self):
        response = self.app.get('/v1/word-frequency-analysis?topic=NonExistentTopic&n=5')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertTrue('error' in data)
        self.assertEqual(data['error'], 'Page not found')

    def test_search_history_empty(self):
        response = self.app.get('/v1/search-history')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 0)

    def test_search_history_not_empty(self):
        # Assuming there are past search results
        app.search_history = [{'topic': 'Python', 'top_words': [('python', 10), ('programming', 5)]}]
        response = self.app.get('/v1/search-history')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertTrue('topic' in data[0])
        self.assertTrue('top_words' in data[0])
        self.assertEqual(data[0]['topic'], 'Python')
        self.assertEqual(len(data[0]['top_words']), 2)

if __name__ == '__main__':
    unittest.main()