# News Article Scraper

This project is a Python web scraping script that collects article-like listings from a website and exports them into an Excel file.

The purpose of this project is to demonstrate how web scraping can be used to collect large datasets from websites that contain multiple pages.

## Features

* Scrapes article titles
* Extracts metadata from listings
* Collects article links
* Handles pagination across multiple pages
* Exports data to Excel

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## Installation

Clone the repository:

```
git clone https://github.com/ExcelsKennedy2/News-Article-Scraper.git
```

Navigate to the folder:

```
cd news-article-scraper
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the scraper:

```
python scraper.py
```

After execution, the script generates:

```
articles.xlsx
```

This Excel file contains all scraped article listings.

## Example Output

| Title           | Price | Rating | Link         |
| --------------- | ----- | ------ | ------------ |
| Example Article | £51   | Three  | article link |

## Learning Objectives

This project demonstrates:

* Pagination scraping
* Extracting structured data from listing pages
* Exporting data to Excel using Pandas

## Disclaimer

This project is for educational purposes. Always respect the terms of service of websites when scraping their content.
