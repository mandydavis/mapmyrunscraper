## The question
As the COVID pandemic continued consuming our days and options for activities, I wondered if people were resorting to outdoor exercise more than ever ([stocks and app downloads suggested this was the case](https://finance.yahoo.com/news/coronavirus-pandemic-running-boom-in-america-morning-brief-100429724.html?guccounter=1)). As an avid runner myself, I had certainly upped my mileage to get some extra training and time outside of my house. To answer this question objectively, I created a web scraper to gather data from a popular fitness site, [mapmyrun.com](mapmyrun.com).

## Technology
* I wrote code in python to take advantage of some really helpful, pre-existing web scraping packages and functions. Using python also meant I could use pandas to efficiently store the data as it was being collected.
* As a Chrome user, I used the Selenium webdriver to be my 'robot' 
* I parsed the HTML code using the BeautifulSoup library

## Outcome
In less than 100 lines of code (excluding comments and spacing), I created a web scraper to navigate mapmyrun.com that downloaded the 7,600 total running activities that users uploaded to the site in the year of 2020. Though stock prices, app downloads, and my personal hunch would suggest otherwise, the data show that New Year's Resolutions were much more impactful in convincing people to lace up their shoes and go out for a run. (Recall that in the US, the pandemic was not a large concern domestically until March 2020). Of course, this theory is not perfect—perhaps New Year's Resolutioners are more app saavy than their pandemic-stir-crazy counterparts. You can view the 2020 mapmyrun running trend yourself in the graph below (yes, it needs some work):
![2020 running trends graph](2020_running_trend_viz)

## How to run this code [work in progress -- need to do some investigating]
(Please note that this code may become outdated with later versions of the mapmyrun website or even Chrome. If Chrome has updated, you will need to change the version in `requirements.txt` for Selenium.)
1. Clone this repository
2. Install the required libraries using your terminal: `pip install -r requirements.txt`
3. To run the scraper: `cd` into the source folder, then: `python3 mapmyrun_scraper.py`
4. To run the visualization, from the mapmyrunscraper folder in your terminal: `python3 viz.py` 

## Learnings about web scraping
* You cannot scrape any website you want. I wanted to scrape Strava (probably the leading app for tracking running), but it's not allowed. Add 'robots.txt' to the end of any url to see what the permissions are. Check out the difference for [Strava](https://www.strava.com/robots.txt) and [mapmyrun](https://www.mapmyrun.com/robots.txt)
* Be responsible! Please do not crash a website by neglecting to add delays/pauses in your code.
* **Taking advantage of page redirects** can save you a lot of time and code. For example, instead of logging in on the website's home page, this was the very first thing I had the driver do: `driver.get("https://www.mapmyrun.com/routes/search")`. It automatically redirects to the login screen, and after successfully logging in, takes you to the desired page. This saves you from programming two additional clicks.

## Resources
* I first watched [this](https://www.youtube.com/watch?v=RUQWPJ1T6Zc&t=281s) tutorial from the 2020 PyCon US conference to gain a basic understanding of web scraping.
* I gathered a few ideas from [this] article on scraping mapmyrun.com using R, though using python meant forging my own path for most of my code.