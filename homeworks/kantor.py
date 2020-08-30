import requests
import datetime
import time
import ast


waluta = 'PLN'
url = f'https://api.exchangeratesapi.io/latest?symbols={waluta}'
timeout = 0.99

def kantor(fn):
    def wrapper():
        wynik = [['Kurs/Błąd pozyskania', 'Data i godzina', 'Czas wykonania']]
        while True:
            now = datetime.datetime.now()
            date_time_now = now.strftime("%d/%m/%Y, %H:%M:%S")
            try:
                start_wykonaina = datetime.datetime.now()
                pobierz_kurs = fn()
                koniec_wykonania = datetime.datetime.now()
                czas_wykonania = start_wykonaina - koniec_wykonania

                pobierz_kurs_txt = pobierz_kurs.text
                currency_as_dictionary = ast.literal_eval(pobierz_kurs_txt)

                print('Kurs Euro:', currency_as_dictionary['rates']['PLN'])
                print('Data i godzina: ', date_time_now)
                print(f'Czas wykonania zapytania: {int(czas_wykonania.microseconds / 1000)} ms')
            except requests.Timeout:
                print('Błąd pozyskania danych')
                print('Data i godzina: ', date_time_now)
                print(f"Czas wykonania zapytania: {int(timeout)} ms")
            print('=====================================')

            time.sleep(15)

    return wrapper()


@kantor
def kurs_wymiany():
    return requests.get(url, timeout=timeout)
