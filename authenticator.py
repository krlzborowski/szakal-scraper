from getpass import getpass

URL = "http://baza-firm.lysik.pl/user/login"


class Authenticator:

    def __init__(self, browser):
        self.credentials = {}
        self.br = browser

    def set_credentials(self):
        username = input('Username: ')
        password = getpass('Password: ')
        self.credentials['username'] = username
        self.credentials['password'] = password

    def log_in(self):
        self.br.open(URL)
        self.br.select_form(nr=0)
        self.br.form['login_username'] = self.credentials['username']
        self.br.form['login_password'] = self.credentials['password']
        r = self.br.submit()
        return r
