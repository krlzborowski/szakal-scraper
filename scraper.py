from getpass import getpass
import mechanize
import http.cookiejar as cj

URL = "http://baza-firm.lysik.pl/user/login"


class Scraper:

    def __init__(self):
        self.credentials = {}
        self.br = None

    def set_credentials(self):
        username = input('Username: ')
        password = getpass('Password: ')
        self.credentials['username'] = username
        self.credentials['password'] = password

    def make_browser(self):
        cookie_jar = cj.CookieJar()
        self.br = mechanize.Browser()
        self.br.set_cookiejar(cookie_jar)
        self.br.addheaders = [('User-agent', 'Firefox')]
        self.br.set_handle_robots(False)

    def login(self):
        self.br.open(URL)
        self.br.select_form(nr=0)
        self.br.form['login_username'] = self.credentials['username']
        self.br.form['login_password'] = self.credentials['password']
        r = self.br.submit()
        return r


