import os
import datetime

def generate_html(articles):
    """
    Generates an HTML page containing a summary of the given news articles.

    Args:
        articles (list): A list of dictionaries where each dictionary contains
            the title, URL, date and summary of a news article.

    Returns:
        str: The HTML content.
    """
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    html = '<html><body><h1>Summary of news for ' + yesterday + '</h1>'
    for article in articles:
        html += f'<h2>{article["title"]}</h2>'
        html += f'<p><a href="{article["url"]}">{article["url"]}</a></p>'
        html += f'<p>{article["date"]}</p>'
        html += f'<p>{article["summary"]}</p>'
        html += '<hr>'
    html += '</body></html>'
    return html

def save_html(html):
    """
    Saves the given HTML content to a file named with yesterday's date.

    Args:
        html (str): The HTML content to be saved.

    The file is saved in the 'summaries' directory with the filename
    format 'YYYY-MM-DD.html', where 'YYYY-MM-DD' is yesterday's date.
    """

    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    filename = f"summaries/{yesterday}.html"
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(html)
    print(f"HTML file saved as {filename}")

def cleanup_old_html(days_to_keep=7):
    """
    Deletes HTML files older than the specified number of days.
    """
    now = datetime.datetime.now()
    dir_path = 'summaries'
    for file in os.listdir(dir_path):
        if file.endswith('.html'):
            try:
                date_str = file.replace('.html', '')
                file_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                if (now - file_date).days > days_to_keep:
                    os.remove(os.path.join(dir_path, file))
                    print(f"Deleted old file: {file}")
            except Exception:
                pass