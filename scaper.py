import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


url = "https://en.wikipedia.org/wiki/Los_Angeles"

response = requests.get(url, headers=headers, timeout=10)
try:
    response.raise_for_status()
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    
except requests.RequestException as e:
    print(f"failed to fetch {url}: {e}")


for targetElement in soup.select('a:not([rel="mw:WikiLink"])'):
    
    href=targetElement.get('href')
    title=targetElement.get('title')
    result = { "href": href, "title": title }
    print(result)
#print(soup.prettify())
