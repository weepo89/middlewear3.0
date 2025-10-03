import requests
from bs4 import BeautifulSoup

def search(size: str):
    url = f"http://www.shopwtwd.com/Shop.aspx?search={size}"
    return {"url": url, "availability": "TBD"}
