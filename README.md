# Yale Student Facebook Scraper

## Overview
This project uses **Selenium** and **Beautiful Soup** to scrape Yale’s online student directory (after manual CAS login).  
The scraper collects structured data from each student card, including:

- Name  
- College  
- Class year  
- Address  
- Major  
- Birthday  
- Photo URL  

All results are exported to a CSV file (`students.csv`) with clear headers for further analysis.


## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/soumildesai/yale-scraper/
   cd yale-scraper
   
2. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Run the scraper
   ```bash
   python scraper_all.py

When prompted in the terminal:
Log in via Yale CAS in the opened browser window.
After scraping, the page will be closed and output will be written to students_full.csv.


Resources used:
Selenium webdriver: https://www.selenium.dev/documentation/webdriver/
Beautiful Soup web scraping: https://realpython.com/beautiful-soup-web-scraper-python/
Writing to CSV: https://docs.python.org/3/library/csv.html#csv.DictWriter
