import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


url = "https://www.youtube.com/"

response = requests.get(url, headers=headers, timeout=10)
try:
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

except requests.RequestException as e:
    print(f"failed to fetch {url}: {e}")


for post in soup.select("div.post"):
    title = post.find("h3")
    if title:
        print(title.get_text(strip=True))

print(soup.prettify())
