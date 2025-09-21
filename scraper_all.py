from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, csv
from bs4 import BeautifulSoup


# Launch browser
driver = webdriver.Chrome()
driver.get("https://students.yale.edu/facebook/")


# Wait for login
print("log in manually in the browser window...")
time.sleep(30)   # Time to login

# Switch dropdown to 'Yale'
select_elem = driver.find_element(By.ID, "college_select")
select = Select(select_elem)
select.select_by_visible_text("Yale")
time.sleep(2)


# Go to the ALL page
driver.get("https://students.yale.edu/facebook/PhotoPageNew?currentIndex=-1&numberToGet=-1")
time.sleep(10)


# Grab HTML
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


# Parse student cards
cards = soup.select(".student_container")
print(f"Found {len(cards)} student cards")

with open("students_full.csv", "w", newline="", encoding="utf-8") as fout:
    writer = csv.DictWriter(
        fout,
        fieldnames=["name", "year", "college", "address", "major", "birthday", "photo_url"],
    )
    writer.writeheader()

    for c in cards:
        # Name
        name_el = c.select_one(".student_name h5")
        name = name_el.get_text(strip=True) if name_el else ""

        # Year
        year_el = c.select_one(".student_year")
        year = year_el.get_text(strip=True) if year_el else ""

        # College (first .student_info)
        college_el = c.select_one(".student_text_container .student_info")
        college = college_el.get_text(strip=True) if college_el else ""

        # Photo
        img_el = c.select_one(".student_img img")
        photo_url = ("https://students.yale.edu" + img_el["src"]) if img_el else ""

        # Address + Major + Birthday (second .student_info)
        info_blocks = c.select(".student_text_container .student_info")
        address = major = birthday = ""
        if len(info_blocks) > 1:
            info_text = info_blocks[1].get_text("\n", strip=True)
            lines = [line.strip() for line in info_text.split("\n") if line.strip()]

            if len(lines) >= 2:
                major = lines[-2] if len(lines[-2]) > 2 else "" # second-to-last line
                birthday = lines[-1] if len(lines[-1]) == 5 or len(lines[-1]) == 6 else ""  # last line
                address = ", ".join(lines[:-2]) if len(lines) > 2 else ""

        writer.writerow({
            "name": name,
            "year": year,
            "college": college,
            "address": address,
            "major": major,
            "birthday": birthday,
            "photo_url": photo_url,
        })

print("Data saved to students_full.csv")
driver.quit()
