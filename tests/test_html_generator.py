import unittest
from app.html_generator import generate_html, save_html, cleanup_old_html
from datetime import datetime, timedelta
import os

class TestHTMLGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a directory for the test if it doesn't exist
        if not os.path.exists("summaries"):
            os.makedirs("summaries")

    def test_generate_html(self):
        # Sample articles for testing
        articles = [
            {
                "title": "Test Article 1",
                "url": "http://example.com/article1",
                "date": "2023-10-01",
                "summary": "This is a summary of article 1."
            },
            {
                "title": "Test Article 2",
                "url": "http://example.com/article2",
                "date": "2023-10-02",
                "summary": "This is a summary of article 2."
            }
        ]

        # Generate HTML
        html = generate_html(articles)

        # Check if the HTML contains the expected content
        self.assertIn("Summary of news for", html)
        self.assertIn("Test Article 1", html)
        self.assertIn("http://example.com/article1", html)
        self.assertIn("This is a summary of article 2.", html)

    def test_save_html(self):
        test_html = "<html><body><h1>Test</h1></body></html>"
        save_html(test_html)
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        filename = f"summaries/{yesterday}.html"
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Test", content)

    def test_cleanup_old_html(self):
        old_date = (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d")
        old_file = f"summaries/{old_date}.html"
        with open(old_file, 'w', encoding="utf-8") as f:
            f.write("<html><body><h1>Old File</h1></body></html>")

        recent_date = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")
        recent_file = f"summaries/{recent_date}.html"
        with open(recent_file, 'w', encoding="utf-8") as f:
            f.write("<html><body><h1>Recent File</h1></body></html>")
        cleanup_old_html(days_to_keep=7)

        self.assertFalse(os.path.exists(old_file), "Old file should be deleted")
        self.assertTrue(os.path.exists(recent_file), "Recent file should not be deleted")

    @classmethod
    def tearDown(cls):
        # Clean up the test directory after each test
        for file in os.listdir("summaries"):
            if file.endswith(".html"):
                os.remove(os.path.join("summaries", file))

if __name__ == "__main__":
    unittest.main()