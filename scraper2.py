import requests
from bs4 import BeautifulSoup
from pathlib import Path
response = Path("site.html").read_text(encoding = "utf-8")
print(response)
soup = BeautifulSoup(response, "html.parser")
    


for targetElement in soup.select('h2'):
    
    title=targetElement.get_text(strip=True)
    result = {"heading2": title }
    print(result)
#print(soup.prettify())

