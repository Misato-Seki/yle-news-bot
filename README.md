# yle-news-bot

## Overview

**yle-news-bot** is a Python bot that automatically fetches the latest English news articles from Finland's public broadcaster YLE, summarizes them, generates daily HTML summary pages for publication via GitHub Pages, and posts the URL of summaries to a Discord channel.

## Features

- Automatically fetches the latest news articles from the YLE English news site
- Extracts article content and summarizes it using a transformer-based model (BART via Hugging Face Transformers)
- Generates and saves daily HTML summary files in the `summaries/` directory
- Automatically removes old HTML files
- Posts daily news summaries URL to a specified Discord channel
- Supports scheduled automation and deployment to GitHub Pages via GitHub Actions

## Directory Structure

```
.
├── app/                # Core logic: fetching, summarizing, HTML generation, bot
├── summaries/          # Daily HTML summaries (published via GitHub Pages)
├── tests/              # Unit tests
├── utils/              # Utility functions (e.g., date handling)
├── main.py             # Main execution script
├── requirements.txt    # Python dependencies
├── .github/workflows/  # GitHub Actions workflows
└── README.md
```

## Setup

1. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Create a `.env` file and set your Discord Bot token and channel ID:

   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token
   DISCORD_CHANNEL_ID=your_channel_id
   ```

3. Run the bot:

   ```sh
   python main.py
   ```
4. Using Docker

Build the Docker image:
```shell
docker build -t yle-news-bot .
```
Run the container:
```shell
docker run --rm \
  -e DISCORD_BOT_TOKEN=your_discord_bot_token \
  -e DISCORD_CHANNEL_ID=your_channel_id \
  -v $(pwd)/summaries:/app/summaries \
  yle-news-bot
```
   *Make sure your Discord bot is enabled and invited to the target channel.*

## Testing

```sh
python -m unittest discover -s tests
```

## GitHub Pages

- HTML summaries in the `summaries/` directory are automatically deployed to the `gh-pages` branch via [GitHub Actions](.github/workflows/deploy.yml).
- Example published URL: `https://<username>.github.io/yle-news-bot/2024-06-15.html`

## Main Modules

- `app/fetch_articles.py`: Fetches YLE news articles
- `app/extract_article_text.py`: Extracts article body text
- `app/summarizer.py`: Summarizes articles
- `app/html_generator.py`: Generates and manages HTML summaries
- `app/bot.py`: Handles Discord posting
- `main.py`: Orchestrates the workflow

## License

MIT License

---

Feedback and pull requests are welcome!
