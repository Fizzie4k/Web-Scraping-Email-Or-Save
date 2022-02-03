# Web Scraping program that can send to email and save to local folder

This is a beginner web scraping project inspired by other web scraping projects on Github but with additional features which is saving the file onto local disk

The python libraries used are:
- requests
- BeautifulSoup
- os
- sys
- datetime
- smtplib
- and etc.

(NOTE: I forgot to set up a virtual environment so my requirements.txt is a bit messy, but you can just easily manually install each module)

Instructions:
1. This program asks for URL input (unfortunately, because web scaping is fragile, it only works for hackernews website)
2. It will asks whether user wants to send the data via gmail or save it to local folder
3. It will then asks for your email address (using user input) for both emails (receiver and sender)
4. It then asks for user's password (Using getpass module to keep password hidden)

There are two files. Different files have different ways in parsing from the HTML content with BeautifulSoup
