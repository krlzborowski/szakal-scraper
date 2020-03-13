from bs4 import BeautifulSoup
import re

URL_TAKEN_COMPANIES = 'http://baza-firm.lysik.pl/bf/companies/taken/1?sort%5Bname%5D=&sort%5Border%5D=&filter%5Bname' \
                      '%5D=&filter%5Bgroup%5D=1&filter%5Buser%5D=&filter%5Bstatus%5D=&filter%5Bfinished%5D=&filter' \
                      '%5Blimit%5D=ALL&submit=Filtruj '


class Scraper:

    def __init__(self, browser):
        self.statuses = {'Przypisana': 0, 'Nawiązano kontakt - dzwonić później': 0,
                         'Nawiązano kontakt - oczekuje na odpowiedź': 0, 'Umówione spotkanie': 0, 'Praktyka': 0,
                         'Nieudana próba nawiązania kontaktu': 0, 'Współpraca za rok': 0, 'Współpraca może za rok': 0,
                         'Niezainteresowana': 0, }
        self.br = browser

    def count_statuses(self):
        r = self.br.open(URL_TAKEN_COMPANIES)
        soup = BeautifulSoup(r, 'html5lib')
        for k in self.statuses.keys():
            res = soup.find_all('td', string=re.compile(k))
            self.statuses[k] = len(res)

    def print_results(self):
        count = 0
        for k, v in self.statuses.items():
            print('{0:<45} {1:>5}'.format(k, str(v)))
            count += v

        print("\nOgółem: {0:>43}".format(str(count)))
