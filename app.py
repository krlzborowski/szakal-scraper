from scraper import Scraper
import mechanize
import http.cookiejar as cj
from authenticator import Authenticator


class App:

    def __init__(self):
        self.br = mechanize.Browser()
        self.sc = Scraper(self.br)
        self.auth = Authenticator(self.br)

    def run(self):
        self.make_browser()
        self.auth.set_credentials()
        self.auth.log_in()
        self.sc.count_statuses()
        self.sc.print_results()

    def make_browser(self):
        cookie_jar = cj.CookieJar()
        self.br.set_cookiejar(cookie_jar)
        self.br.addheaders = [('User-agent', 'Firefox')]
        self.br.set_handle_robots(False)
