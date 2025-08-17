import pandas as pd
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# ---------------- Selenium scraping ----------------
driver = webdriver.Chrome()
driver.get("https://steamdb.info/")
time.sleep(5)

# Popular Releases
popular_table = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div[1]/table/tbody')
popular_rows = popular_table.find_elements(By.TAG_NAME, "tr")

popular_data = []
for row in popular_rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 3:
        game_name = cols[0].text
        peak_24h  = cols[1].text
        price     = cols[2].text

        popular_data.append({
            "Popular_Releases": game_name,
            "24h_Peak": peak_24h,
            "Price": price
        })

popular_df = pd.DataFrame(popular_data)

# Hot Releases
hot_table = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div[2]/table/tbody')
hot_rows = hot_table.find_elements(By.TAG_NAME, "tr")

hot_data = []
for row in hot_rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 3:
        game_name = cols[0].text
        rating    = cols[1].text
        price     = cols[2].text

        hot_data.append({
            "Hot_Releases": game_name,
            "Rating": rating,
            "Price": price
        })

hot_df = pd.DataFrame(hot_data)

popular_df.to_csv("popular.csv", index=False)
hot_df.to_csv("hot.csv", index=False)

driver.quit()  # close browser

