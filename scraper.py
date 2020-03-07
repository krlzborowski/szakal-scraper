# Python program to scrape website
# and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
import mechanize
import http.cookiejar as cj

URL = "http://baza-firm.lysik.pl/user/login"
r = requests.get(URL)

cookie_jar = cj.CookieJar()
browser = mechanize.Browser()
browser.set_cookiejar(cookie_jar)

soup = BeautifulSoup(r.content, 'html5lib')

# print(soup.title.string)

print(soup.prettify())
