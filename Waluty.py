"""
# Potrzebujemy przeliczyć trochę waluty, czasy niepewne,
# warto mieć na uwadze swoją ulubioną walutę.
# Napisz klasę, która będzie zawierać dwie metody:

#       przeliczenie wybranej waluty z tabeli A na złotówki  <- dane wejściowe: kod waluty, ilość waluty
#       wskazanie aktualnego kursu z tabeli A <- dane wjećiowe: kod waluty

# Klasa w celu przeliczenia waluty powinna skorzystać z aktualnych kursów z Narodowego Banku Polskiego
# dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/

# Gdy skończysz prześlij mi swoje zadanie w postaci linku do swojego GitHuba, innych linków nie przyjmuję :)
# Na rozwiązanie czekam do końca dnia do niedzieli 22.01.2023
"""

import requests


class Waluty:
    def __init__(self, kod_waluty: str, ilosc_waluty: int):
        self.kod_waluty = kod_waluty
        self.ilosc_waluty = ilosc_waluty
        self.tabela = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/').json()
        self.przelicznik = ''

        for i in self.tabela[0]['rates']:
            if i['code'] == self.kod_waluty:
                self.przelicznik = i['mid']
                break

    def przeliczenie_waluty(self) -> str:
        przeliczona_waluta = self.ilosc_waluty * self.przelicznik
        return f'{przeliczona_waluta} PLN'

    def kurs_waluty(self) -> str:
        return f'1 {self.kod_waluty} = {self.przelicznik} PLN'


tysiac_dolarow = Waluty('USD', 1000)
print(tysiac_dolarow.przeliczenie_waluty())
print(tysiac_dolarow.kurs_waluty())


class Waluty2:
    tabela = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/').json()

    @staticmethod
    def znajdz_przelicznik(kod_waluty):
        for i in Waluty2.tabela[0]['rates']:
            if i['code'] == kod_waluty:
                return i['mid']

    @staticmethod
    def przeliczenie_waluty(kod_waluty: str, ilosc_waluty: int) -> str:
        przelicznik = Waluty2.znajdz_przelicznik(kod_waluty)
        przeliczona_waluta = ilosc_waluty * przelicznik
        return f'{przeliczona_waluta} PLN'

    @staticmethod
    def kurs_waluty(kod_waluty: str) -> str:
        przelicznik = Waluty2.znajdz_przelicznik(kod_waluty)
        return f'1 {kod_waluty} = {przelicznik} PLN'


print(Waluty2.przeliczenie_waluty(kod_waluty='USD', ilosc_waluty=1000))
print(Waluty2.kurs_waluty('USD'))
