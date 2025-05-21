import os

def generate_html(articles):
    html = '<html><body>'
    for article in articles:
        html += f'<h2>{article["title"]}</h2>'
        html += f'<p><a href="{article["url"]}">{article["url"]}</a></p>'
        html += f'<p>{article["date"]}</p>'
        html += f'<p>{article["summary"]}</p>'
        html += '<hr>'
    html += '</body></html>'
    return html

def save_html(html, filename='latest_summary.html'):
    with open(filename, 'w') as f:
        f.write(html)
    print(f"HTML file saved as {filename}")