from tuomari import Tuomari
from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def  _pelaajan2_siirto(self):
        return input("Toisen pelaajan siirto: ")
