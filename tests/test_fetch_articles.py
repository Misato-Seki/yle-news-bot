# なんかうまくいかない。
import unittest
from unittest.mock import patch, Mock
from app.fetch_articles import fetch_articles  # ← 適切なモジュール名に変更してください

# テスト用のモックHTML
MOCK_HTML = """
<html>
  <body>
    <h3>
      <a href="https://yle.fi/news/1-12345678">Sample News Title</a>
      <time datetime="2024-06-15T12:00:00+0000">15.6.</time>
    </h3>
  </body>
</html>
"""


class TestFetchArticles(unittest.TestCase):
    
    @patch("utils.date_utils.is_yesterday", return_value=True)
    @patch("app.fetch_articles.requests.get")
    def test_fetch_articles(self, mock_get, mock_is_yesterday):
        # モックレスポンスの設定
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = MOCK_HTML
        mock_get.return_value = mock_response

        # モックの設定
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = MOCK_HTML
        print("Mocked response text:", mock_get.return_value.text[:100])  # 最初の100文字だけ表示

        # テスト対象の関数を呼び出し
        articles = fetch_articles()
        print("==== DEBUG OUTPUT ====")
        print(f"Number of articles fetched: {len(articles)}")
        for article in articles:
            print(article)
        print("======================")


        # アサーション
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["title"], "Sample News Title")
        self.assertEqual(articles[0]["url"], "https://yle.fi/news/1-12345678")
        self.assertEqual(articles[0]["date"], "2024-06-15")
        self.assertIsNone(articles[0]["summary"])

if __name__ == "__main__":
    unittest.main()
