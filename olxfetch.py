from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# set up Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome() 

def save_to_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def extract_data():
    try:
        driver.get("https://www.olx.in/api/relevance/v4/search?category=84&facet_limit=1000&lang=en-IN&location=4058748&location_facet_limit=100&make=tata,mahindra&model=mahindra-xuv700,tata-harrier&nested-filters={%22make%22:[{%22tata%22:{%22model%22:[%22tata-harrier%22]}},{%22mahindra%22:{%22model%22:[%22mahindra-xuv700%22]}}]}&page=1&platform=web-desktop&price_max=1600000&price_min=200000&pttEnabled=true&relaxedFilters=true&size=40&user=04139798367801143&year_max=2024&year_min=2018")
        data_element = driver.find_element(By.XPATH, "//div[@class='data-container']")
        driver.quit()
        data = data_element.text
        save_to_json(data)
        return "done"
    except Exception as e:
        return str(e)