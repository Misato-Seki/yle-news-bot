# python -m unittest test_summarizer.py
import unittest
from app.bot import format_summary

class TestSummaryFormatter(unittest.TestCase):
    def test_format_summary(self):
        articles = [
            {
                'title': 'Article 1',
                'url': 'http://example.com/article1',
                'date': '2023-10-01',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 2',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 3',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 4',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 5',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 6',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 7',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            },
            {
                'title': 'Article 8',
                'url': 'http://example.com/article2',
                'date': '2023-10-02',
                'summary': 'Finnish government will cover the entire cost of providing flights between Helsinki and five regional airports. Minister of Transport and Communications Lulu Ranne said the decision was made in the interests of regional vitality. All five routes are run at a significant loss, running into millions of euros each. A return flight from Helsinki to Kemi costs the Finnish state 8,586 euros, as ticket sales are not enough to make the flights profitable.'
            }
        ]

        formatted_messages = format_summary(articles)
        
        # Check if the number of messages is correct
        self.assertGreaterEqual(len(formatted_messages), 1)

        # Check if the message length is within the limit
        for message in formatted_messages:
            self.assertLessEqual(len(message), 2000)

        # Check if the message contains all articles
        for article in articles:
            self.assertTrue(any(article['title'] in message for message in formatted_messages))
            self.assertTrue(any(article['url'] in message for message in formatted_messages))
            self.assertTrue(any(article['date'] in message for message in formatted_messages))
            self.assertTrue(any(article['summary'] in message for message in formatted_messages))
