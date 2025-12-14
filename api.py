from fastapi import FastAPI, HTTPException
from repository import BabyNameRepository

app = FastAPI(title="Baby Name Statistics API")

repo = BabyNameRepository()


@app.get("/nameinfo")
def name_info(name: str):
    rows = repo.find_by_name(name)

    if not rows:
        raise HTTPException(status_code=404, detail="Name not found")

    first_year = min(y for y, _ in rows)
    most_popular_year = max(rows, key=lambda r: r[1])[0]

    top_years = sorted(rows, key=lambda r: r[1], reverse=True)[:10]
    top_years = [year for year, _ in top_years]

    return {
        "name": name.capitalize(),
        "first_year": first_year,
        "most_popular_year": most_popular_year,
        "top_years": top_years
    }
