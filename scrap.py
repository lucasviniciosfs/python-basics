from bs4 import BeautifulSoup
import requests

class Quote:
    def __init__(self, text, name, link):
        self.text = text
        self.name = name      
        self.link = link

request = requests.get("http://quotes.toscrape.com")
html = BeautifulSoup(request.text, "html.parser")
quotes = []
for quote in html.select(".quote"):
    quotes.append(
        Quote(
          quote.select(".text")[0].getText(),
          quote.select("[itemprop='author']")[0].getText(),
           quote.select("[itemprop='author']")[0].findNextSibling()["href"]
        )
    )

print(quotes[0].name)
print(quotes[0].name)


