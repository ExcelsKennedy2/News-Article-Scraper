import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
prices = []
ratings = []
links = []

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# scrape first 5 pages
for page in range(1, 6):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        link = book.h3.a["href"]

        titles.append(title)
        prices.append(price)
        ratings.append(rating)
        links.append("https://books.toscrape.com/catalogue/" + link)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Link": links
})

df.to_excel("articles.xlsx", index=False)

print("Articles scraped successfully!")