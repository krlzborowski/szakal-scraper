from bs4 import BeautifulSoup

URL_TAKEN_COMPANIES = 'http://baza-firm.lysik.pl/bf/companies/taken/1?sort%5Bname%5D=&sort%5Border%5D=&filter%5Bname' \
                      '%5D=&filter%5Bgroup%5D=1&filter%5Buser%5D=&filter%5Bstatus%5D=&filter%5Bfinished%5D=&filter' \
                      '%5Blimit%5D=ALL&submit=Filtruj '


class Scraper:

    def __init__(self, browser):
        self.statuses = {}
        self.br = browser

    def count_statuses(self):
        r = self.br.open(URL_TAKEN_COMPANIES)
        soup = BeautifulSoup(r, 'html5lib')
        page_code = soup.prettify()
        print(page_code)

