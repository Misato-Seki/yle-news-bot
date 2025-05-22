import unittest
from unittest.mock import patch, Mock
from app.extract_article_text import extract_article_text


class TestExtractArticleText(unittest.TestCase):
    @patch('app.extract_article_text.requests.get')
    def test_extract_article_text_success(self, mock_get):
        html = '''
        <html>
            <body>
                <section class="yle__article__content">
                    <p class="yle__article__paragraph">First paragraph.</p>
                    <p class="yle__article__paragraph">Second paragraph.</p>
                </section>
            </body>
        </html>
        '''

        # Mock the response from requests.get
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html
        mock_get.return_value = mock_response

        # Call the function with a sample URL
        url = 'http://example.com'
        result = extract_article_text(url)

        # Check that the function returns the expected result
        self.assertEqual(result, "First paragraph. Second paragraph.")

if __name__ == '__main__':
    unittest.main()