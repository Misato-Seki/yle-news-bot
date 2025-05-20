from app.fetch_articles import fetch_articles
from app.extract_article_text import extract_article_text
from app.summarizer import summarize_text

def main():
    articles = fetch_articles()
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Date: {article['date']}")
        print("-" * 40)

        # Extract article text
        text = extract_article_text(article['url'])
        if not text:
            print("No content found in the article.")
            continue

        # Summarize the article
        summary = summarize_text(text)
        print("Summary:")
        print(summary)
        print("=" * 80)
        print("\n" * 1)

if __name__ == "__main__":
    main()
