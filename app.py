from scraper import Scraper
import requests
from bs4 import BeautifulSoup

def run():
    sc = Scraper()
    sc.set_credentials()
    sc.make_browser()
    r = sc.login()
    print(r.info())

    # r = login()
    soup = BeautifulSoup(r, 'html5lib')

    page_code = soup.find(text=sc.credentials['username'])
    print(page_code)
