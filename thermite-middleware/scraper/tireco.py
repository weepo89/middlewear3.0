import requests
from bs4 import BeautifulSoup

def search(size: str):
    url = f"http://www.tireco.com/shop?search={size}"
    return {"url": url, "availability": "TBD"}
