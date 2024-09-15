#jeffins_crypto_tracker.py Date last Updated: 22/04/2024
#view readme file in github repo for project overview and instructions to run
#designed and created fully by Jeffin Joseph with the help of online resources, references listed end of file.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the ChromeDriver in natve pc
chrome_service = Service(r'C:\webdrivers\chromedriver.exe')  # update this path to where chromedriver is installed

# Initialise the WebDriver
driver = webdriver.Chrome(service=chrome_service)

# Open the CoinMarketCap website
url = 'https://coinmarketcap.com/'
driver.get(url)

# wait for the table to be fully loaded
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
)

cryptos = []
rows = driver.find_elements(By.XPATH, "//tbody/tr")  # must use xpath as class names are being updated by the second in real time due to price changes

#manipulates a for loop to read every xrow path from crypto no1 down to crypto 10
for i, row in enumerate(rows[:10], start=1): 
    try:
        # using dynamic XPaths for each row, these xpaths were found by using inspect element and copying the class names by xpath on chrome
        name_xpath = f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{i}]/td[3]/div/a/div/div/div/p'
        price_xpath = f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{i}]/td[4]/div'
        market_cap_xpath = f'//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{i}]/td[8]/p/span[2]'

        name_element = driver.find_element(By.XPATH, name_xpath)
        price_element = driver.find_element(By.XPATH, price_xpath)
        market_cap_element = driver.find_element(By.XPATH, market_cap_xpath)

        name = name_element.text.strip()
        price = price_element.text.strip()
        market_cap = market_cap_element.text.strip()

        cryptos.append([name, price, market_cap])
    except Exception as e:
        print(f"Error processing row {i}: {e}")

# closes the browser after scraping
driver.quit()

# convert the list to a pandas dataframe in order to plot via matplotlib
df = pd.DataFrame(cryptos, columns=['Name', 'Price', 'Market Cap'])

# cleaning up the data (removes $, commas)
df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)
df['Market Cap'] = df['Market Cap'].str.replace('$', '').str.replace(',', '').str.replace('B', '').astype(float)

# checks if the DataFrame is populated this is for debugging purposes
print(df)

# plots the data using Matplotlib
plt.bar(df['Name'], df['Market Cap'])
plt.xlabel('Cryptocurrency')
plt.ylabel('Market Cap (in billions)')
plt.title('Top 10 Cryptocurrencies by Market Cap')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#REFERENCES:
#Selenium Tut: https://www.youtube.com/watch?v=NB8OceGZGjA
#Matplotlib Tut: https://www.youtube.com/watch?v=OZOOLe2imFo
#Pandas Tut: https://www.youtube.com/watch?v=iGFdh6_FePU
#Installing Chromedriver: https://www.youtube.com/watch?v=dz59GsdvUF8