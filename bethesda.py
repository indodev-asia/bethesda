#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


URL = "https://gear.bethesda.net/collections/all"
CUSTOM_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


options = Options()
options.add_argument(f"user-agent={CUSTOM_UA}")
options.add_argument("--headless=new")  
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=options)
driver.get(URL)


time.sleep(5)


links = driver.find_elements(By.TAG_NAME, "a")


product_links = []
for link in links:
    href = link.get_attribute("href")
    if href and "/products/" in href:
        product_links.append(href)

product_links = list(set(product_links))

print(f"Found {len(product_links)} product links:")
for p in product_links:
    print(p)

driver.quit()
