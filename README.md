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
   git clone <your-repo-url>
   cd yale-scraper
   
2. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Run the scraper
   python scraper_all.py

When prompted in the terminal:
Log in via Yale CAS in the opened browser window.
After scraping, the page will be closed and output will be written to students_full.csv.
