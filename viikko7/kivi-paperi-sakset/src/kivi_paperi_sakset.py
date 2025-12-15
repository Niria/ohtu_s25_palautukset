from abc import ABC, abstractmethod
from tuomari import Tuomari


class KiviPaperiSakset(ABC):
    def pelaa(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        tuomari = Tuomari()

        ekan_siirto = self._pelaajan1_siirto()
        tokan_siirto = self._pelaajan2_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._pelaajan1_siirto()
            tokan_siirto = self._pelaajan2_siirto()

        print("Kiitos!")
        print(tuomari)

    def _pelaajan1_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    @abstractmethod
    def _pelaajan2_siirto(self):
        return Exception("Aliluokka ei ole määritellyt tätä metodia")

    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
