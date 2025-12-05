# Insert google maps review section url here.
# url = "GOOGLE_MAPS_REVIEW_URL"
url = "https://www.google.com/maps/place/Ganeshsthan+Temple/@27.7005687,84.4468399,15z/data=!4m8!3m7!1s0x3994e5cf97bbac17:0x3a169f1b4476c85c!8m2!3d27.706111!4d84.4429832!9m1!1b1!16s%2Fm%2F03gqnjd?entry=ttu&g_ep=EgoyMDI1MTIwMi4wIKXMDSoASAFQAw%3D%3D"

# import libraries
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time
import json

# webdriver setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)

# Find the scrollable reviews container
scrollable_div = driver.find_element(
    By.CSS_SELECTOR, ".m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde"
)

# Find the initial height of the container
previous_height = driver.execute_script(
    "return arguments[0].scrollHeight", scrollable_div
)
scroll_attempts = 0
max_scrolls = 10  # Limit scrolls to avoid infinite loops

# Scroll through reviews
while scroll_attempts < max_scrolls:
    # Scroll down
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div
    )
    time.sleep(2)

    # Calculate new height
    new_height = driver.execute_script(
        "return arguments[0].scrollHeight", scrollable_div
    )

    # Check if we've reached the end
    if new_height == previous_height:
        break

    previous_height = new_height
    scroll_attempts += 1

# Extract reviews using BeautifulSoup
time.sleep(1)
soup = bs(driver.page_source, "html.parser")
items = soup.find_all("div", class_="jJc9Ad")
reviews = soup.find_all("div", class_="jftiEf fontBodyMedium")
list = []
for review in reviews:
    try:
        name = review.find("div", class_="d4r55")
        stars = review.find("span", class_="kvMYJc")
        star = stars.find_all("span", class_="hCCjke google-symbols NhBTye elGi1d")
        desc = review.find("div", class_="MyEned")
        img = review.find("img", class_="NBa7we")["src"]
        s = len(star)
        try:
            d = desc.text
        except:
            d = ""
            pass
        obj = {}
        obj["name"] = f"{name.text}"
        obj["img"] = f"{img}"
        obj["stars"] = f"{s}"
        obj["review"] = f"{d}"
        list.append(obj)
    except:
        print("error fetching reviews")
        pass

with open("data.json", "w", encoding="UTF-8") as f:
    json.dump(list, f, indent=4)
driver.quit()
