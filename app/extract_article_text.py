import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    content_section = soup.find("section", class_="yle__article__content")
    if not content_section:
        return ""
    
    paragraphs = content_section.find_all("p", class_="yle__article__paragraph")
    text = " ".join([p.get_text(strip=True) for p in paragraphs])

    return text.strip()


if __name__ == "__main__":
    url = input("Enter the URL of the article: ")
    text = extract_article_text(url)
    print(text)