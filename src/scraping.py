from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# Target URL
query_cars = 'cars/EB9C8147-07C0-4951-A962-381CDB400E37/F93D355F-CC20-4FFE-9CB7-6C7CDFF1DC50'
driver.get(f'https://hamrobazaar.com/category/{query_cars}')

time.sleep(3)  # Initial load

# Infinite scroll until no new items
prev_count = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for new items to load
    elements = driver.find_elements(By.CSS_SELECTOR, ".card-product")  # Use correct selector
    print(f"Currently loaded: {len(elements)} items")
    if len(elements) == prev_count:
        break
    prev_count = len(elements)

# Extract product details
products = []
for el in elements:
    try:
        title = el.find_element(By.CSS_SELECTOR, ".card-product-title").text
        price = el.find_element(By.CSS_SELECTOR, ".card-product-price").text
        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
        products.append({"title": title, "price": price, "link": link})
    except:
        continue

print(f"Total products scraped: {len(products)}")

# Optional: Save to CSV
import pandas as pd
df = pd.DataFrame(products)
df.to_csv("hamrobazaar_cars.csv", index=False)

# Close driver
driver.quit()
