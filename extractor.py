import requests
import json
from datetime import date
import os

APP_ID = "a1543e4a"
APP_KEY = "381fe7d44fbf77b75c1ac3d83a872aaf"

def fetch_jobs(keyword="data engineer", country="gb", results_per_page=10):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": keyword,
        "results_per_page": results_per_page,
        "content-type": "application/json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    data = fetch_jobs()
    os.makedirs("data/raw", exist_ok=True)
    filename = f"data/raw/jobs_{date.today()}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Guardados {len(data['results'])} empleos en {filename}")