import requests
import os

SHOPIFY_STORE = "ygj1ha-xp.myshopify.com"
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

def sync_to_shopify(data):
    url = f"https://{SHOPIFY_STORE}/admin/api/2025-01/products.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }

    for distributor, result in data.items():
        payload = {
            "product": {
                "title": f"{distributor} Tire {result['url']}",
                "body_html": f"Synced from {distributor}",
                "vendor": distributor,
                "status": "draft"
            }
        }
        r = requests.post(url, headers=headers, json=payload)
        print(r.json())
