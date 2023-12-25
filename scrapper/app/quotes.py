import requests
from bs4 import BeautifulSoup
import json

def __scrape_page(category: str):
    res = requests.get(f"https://www.goodreads.com/quotes/tag/{category}")
    data = BeautifulSoup(res.text, "html.parser")
    return data

def quotes(category: str):
    data = __scrape_page(category)
    quote_body = data.select(".quoteDetails")
    quotes = []
    for (index, quote) in enumerate(quote_body):
        row = {'id': index+1, 'quote': None}
        row["quote"] = quote.find("div", class_="quoteText").getText().strip().encode("ascii", "ignore").decode().replace("  ", "")
        quotes.append(row)
    return {"total": len(quotes), "quotes": quotes}