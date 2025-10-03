from fastapi import FastAPI, Query
from scraper import wtwd, wtd, tireco
from shopify_sync import sync_to_shopify

app = FastAPI(title="Thermite Tactical Middleware")

@app.get("/")
def home():
    return {"status": "Thermite Middleware Running"}

@app.get("/search")
def search_tires(width: str = Query(...), aspect: str = Query(...), diameter: str = Query(...)):
    query = f"{width}/{aspect}/{diameter}"
    
    results = {
        "WTWD": wtwd.search(query),
        "WTD": wtd.search(query),
        "Tireco": tireco.search(query)
    }

    sync_to_shopify(results)
    return {"query": query, "results": results}
