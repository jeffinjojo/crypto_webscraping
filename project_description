Prerequisites
To run this project, you’ll need the following installed on your machine:

Python 3.x
Google Chrome (or another supported browser)
ChromeDriver (or another WebDriver matching your browser version)
Python Libraries:
Selenium: pip install selenium
pandas: pip install pandas
Matplotlib: pip install matplotlib
ChromeDriver Setup
Download ChromeDriver from here and place it in a known directory on your system.
Make sure the version of ChromeDriver matches your version of Google Chrome.
Installation
Clone this repository or download the script:
bash
Copy code
git clone https://github.com/yourusername/crypto-market-tracker.git
cd crypto-market-tracker
Install the required Python libraries:
bash
Copy code
pip install selenium pandas matplotlib
Ensure ChromeDriver is installed and the path is set correctly in the script.
How to Run
Ensure ChromeDriver is correctly installed and the executable path is specified in the script.

Run the script:

bash
Copy code
python crypto_tracker.py
The program will automatically open a Chrome browser, scrape data from CoinMarketCap, and generate a bar chart showing the market capitalisation of the top 10 cryptocurrencies.
Usage Notes
The script waits for the dynamic content of the page to load before scraping. This is handled using Selenium’s explicit waits to ensure that the elements are fully loaded.
The data is cleaned and structured using pandas, and the final output is visualised with Matplotlib.
The project can be extended by integrating the CoinMarketCap API or deploying it with Flask for user interaction.
Troubleshooting
ChromeDriver path issues: Ensure that the path to ChromeDriver is correctly specified in the script, and the version matches your installed version of Google Chrome.
Web scraping errors: If the structure of the CoinMarketCap page changes, the script may require updates to the XPath selectors used for scraping the data.
