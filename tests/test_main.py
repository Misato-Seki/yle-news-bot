import unittest
from unittest.mock import patch, AsyncMock
import asyncio
from main import main

class TestMainFunction(unittest.IsolatedAsyncioTestCase):
    @patch("main.fetch_articles")
    @patch("main.extract_article_text")
    @patch("main.summarize_text")
    @patch("main.send_summary_message", new_callable=AsyncMock)
    @patch("main.generate_html")
    @patch("main.save_html")
    @patch("main.cleanup_old_html")
    async def test_main(self, mock_cleanup_old_html, mock_save_html, mock_generate_html, mock_send_summary_message,
                        mock_summarize_text, mock_extract_article_text, mock_fetch_articles):
        # Mock the return values
        mock_fetch_articles.return_value = [
            {"title": "Test Article", "url": "http://example.com", "date": "2024-06-15", "summary": None}
        ]
        mock_extract_article_text.return_value = "This is a test article content."
        mock_summarize_text.return_value = "This is a summary of the test article."

        # Call the main function
        await main()

        print("==== DEBUG OUTPUT ====")
        print(f"Number of articles fetched: {len(mock_fetch_articles.return_value)}")
        for article in mock_fetch_articles.return_value:
            print(article)
        print("======================")

        # Assertions
        mock_fetch_articles.assert_called_once()
        mock_extract_article_text.assert_called_once_with("http://example.com")
        mock_summarize_text.assert_called_once_with("This is a test article content.")
        mock_generate_html.assert_called_once()
        mock_save_html.assert_called_once()
        mock_cleanup_old_html.assert_called_once()
        mock_send_summary_message.assert_awaited_once()  # Check if the async function was awaited

if __name__ == "__main__":
    unittest.main()