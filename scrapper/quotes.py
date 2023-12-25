import requests
from bs4 import BeautifulSoup
import json

class Quotes:
    def __init__(self, category: str):
        self.category = category

    def __scrape_page(self):
        res = requests.get("https://www.goodreads.com/quotes/tag/"+self.category)
        data = BeautifulSoup(res.text, "html.parser")
        return data
    
    def quotes(self):
        data = self.__scrape_page()
        quote_body = data.select(".quoteDetails")
        quotes = []
        for q in quote_body:
            quote = q.find("div", class_="quoteText").getText().strip().encode("ascii", "ignore").decode().replace("  ", "")
            quotes.append(
                {
                    "quote": quote,
                }
            )
        quotes_json = json.dumps(quotes)
        print(quotes_json)

q = Quotes("motivational")
q.quotes()