# main.py
from fastapi import FastAPI
from scraper import Scraper
import pandas as pd

app = FastAPI()
post = Scraper()


@app.get("/{insat}")
async def read_item(insat):
    return post.scrapers("insat.rnu.tn")


"""
df = pd.DataFrame(post.scrapers("insat.rnu.tn"))
#df.to_excel('<filename>.xlsx', header=True, index=False)
print(df.head())
"""
