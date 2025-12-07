class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._alkuperaiset_arvot = []

    def suorita(self):
        self._alkuperaiset_arvot.append(self._sovelluslogiikka.arvo())
        arvo = self._lue_syote()
        self._sovelluslogiikka.plus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkuperaiset_arvot.pop())


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._alkuperaiset_arvot = []

    def suorita(self):
        self._alkuperaiset_arvot.append(self._sovelluslogiikka.arvo())
        arvo = self._lue_syote()
        self._sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkuperaiset_arvot.pop())


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._alkuperaiset_arvot = []

    def suorita(self):
        self._alkuperaiset_arvot.append(self._sovelluslogiikka.arvo())
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._alkuperaiset_arvot.pop())


class Kumoa:
    def __init__(self, suoritetut_komennot):
        self._suoritetut_komennot = suoritetut_komennot

    def suorita(self):
        if self._suoritetut_komennot:
            viimeisin_komento = self._suoritetut_komennot.pop()
            viimeisin_komento.kumoa()
