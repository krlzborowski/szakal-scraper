from scraper import Scraper
from bs4 import BeautifulSoup
import mechanize
import http.cookiejar as cj
from authenticator import Authenticator


class App:

    def __init__(self):
        self.br = mechanize.Browser()
        self.sc = Scraper()
        self.auth = Authenticator(self.br)

    def run(self):
        self.make_browser()
        self.auth.set_credentials()
        r = self.auth.log_in()
        soup = BeautifulSoup(r, 'html5lib')
        page_code = soup.prettify()
        print(page_code)

    def make_browser(self):
        cookie_jar = cj.CookieJar()
        self.br.set_cookiejar(cookie_jar)
        self.br.addheaders = [('User-agent', 'Firefox')]
        self.br.set_handle_robots(False)
