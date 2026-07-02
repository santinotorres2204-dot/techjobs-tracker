import pandas as pd
import json

def clean_jobs(filepath):
    with open(filepath, "r") as f:
        raw = json.load(f)

    jobs = raw["results"]
    df = pd.DataFrame([{
        "id": j["id"],
        "title": j["title"],
        "company": j.get("company", {}).get("display_name", "Unknown"),
        "location": j.get("location", {}).get("display_name", "Unknown"),
        "salary_min": j.get("salary_min"),
        "salary_max": j.get("salary_max"),
        "category": j.get("category", {}).get("label", "Unknown"),
        "description": j.get("description", ""),
        "created": j.get("created")
    } for j in jobs])

    return df

if __name__ == "__main__":
    df = clean_jobs("data/raw/jobs_2026-07-02.json")
    df.to_csv("data/processed/jobs_2026-07-02.csv", index=False)
    print(df[["title", "company", "location", "salary_min", "salary_max"]].to_string())