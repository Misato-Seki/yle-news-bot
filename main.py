from app.fetch_articles import fetch_articles
from app.extract_article_text import extract_article_text
from app.summarizer import summarize_text
from app.bot import TOKEN, send_summary_message, client
from app.html_generator import generate_html, save_html, cleanup_old_html
import asyncio

async def main():
    """
    Fetches the latest news articles from YLE, extracts and summarizes
    the content of each article, and sends the summary to a Discord channel.

    Does the following steps:
    1. Fetches the latest news articles from YLE.
    2. Extracts the content of each article.
    3. Summarizes the content of each article.
    4. Sends the summary to a Discord channel.
    """
    articles = fetch_articles()
    for article in articles:
        # Extract article text
        text = extract_article_text(article['url'])
        if not text:
            print("No content found in the article.")
            continue

        # Summarize the article
        summary = summarize_text(text)
        article['summary'] = summary

        # Print the article title and summary
        print(f"Title: {article['title']}")
        print("-" * 40)

    # Generate HTML file
    html = generate_html(articles)
    save_html(html)

    # Cleanup old HTML files
    cleanup_old_html()

    # Send summary to Discord
    await send_summary_message()

if __name__ == "__main__":    
    async def run_bot():
        """
        Logins to Discord and connects to the gateway, then runs the bot until stopped.
        """
        await client.login(TOKEN)
        await client.connect()

    loop = asyncio.get_event_loop() # 「イベントループ」と呼ばれる「同時にいろんなことを管理して進める」仕組みを用意
    
    loop.create_task(run_bot()) # 「さっきのDiscordボットをつなげる作業(run_bot)をイベントループに登録して、同時に進めてね」という命令
    loop.run_until_complete(main()) # 「ニュースを取ってきて要約してDiscordに送るメインの作業(main)を実行して、その作業が終わるまでこのループを動かし続けるよ」という意味
