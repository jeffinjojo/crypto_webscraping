# crypto_webscraping

"""
Crypto Market Tracker

This project was my first experience using Python libraries like Selenium, Matplotlib and pandas. Due
to my keen interest in financial markets, in particular the cryptocurrency market, I wanted to build 
a web scraper that tracks live cryptocurrency data from coinmarketcap.com and visualises the market cap
of the top 10 cryptocurrencies in the market.

I started by learning Selenium, which is needed to interact with a dynamic, JavaScript-heavy website such
as Coinmarketcap, using XPath to navigate changing page structures. 
Next, I processed the scraped data using pandas, converting it into a structured DataFrame for easier manipulation. 
Finally, I used Matplotlib to visualise the data in a bar chart.

Key Takeaways from this project:
- Gained hands-on experience with Selenium for web scraping and data handling.
- Learned to clean and manipulate data using pandas.
- Developed skills in data visualisation with Matplotlib.
- Built a robust solution that adapts to changing webpage structures.

What challenges did I face:
- Dealing with dynamically changing class names on the webpage made scraping challenging, so I had to use 
  flexible XPaths to reliably extract the data.
- Some elements didn’t load due to java rendering, which required careful handling of page load times 
  using Selenium's explicit waits.
- Processing and cleaning financial data required learning how to use pandas effectively for data manipulation.
- WebDriver was essential for automating browser interactions and scraping content that was dynamically rendered 
  by javascript, which normal scraping libraries couldnt handle.

  Where Could I improve this program:
- Implement API integration: Using the coinmarketcap API instead of web scraping would make the program more 
  efficient and reliable by reducing the risk of website structure changes.
- Add a front end: Adding a front end with flask could make the program interactive for a user.
- Deploy the project: Making this project available online through a cloud service like Azure or AWS would increase 
  its accessibility and further teach me cloud deployment skills.


Overall, this project gave me practical experience in automating data extraction and visualisation, crucial for roles 
involving data analysis and fintech.

REFERENCES:
Selenium Tut: https://www.youtube.com/watch?v=NB8OceGZGjA
Matplotlib Tut: https://www.youtube.com/watch?v=OZOOLe2imFo
Pandas Tut: https://www.youtube.com/watch?v=iGFdh6_FePU
Installing Chromedriver: https://www.youtube.com/watch?v=dz59GsdvUF8
"""
