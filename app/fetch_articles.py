import requests
from bs4 import BeautifulSoup
from utils.date_utils import is_yesterday

BASE_URL = "https://yle.fi/news/tuoreimmat"

def fetch_articles():
    print("Fetching articles from YLE...")
    response = requests.get(BASE_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    for h3 in soup.find_all("h3"):
        a_tag = h3.find("a", href=True)
        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        url = a_tag["href"]

        time_tag = h3.find_next("time")
        if not time_tag:
            continue

        date_time = time_tag["datetime"]
        date = date_time.split("T")[0]

        if is_yesterday(date):
            articles.append({
                "title": title,
                "url": url,
                "date": date,
                "summary": None,  # Placeholder for summary
            })
        
    return articles

if __name__ == "__main__":
    articles = fetch_articles()
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Date: {article['date']}")
        print("-" * 40)