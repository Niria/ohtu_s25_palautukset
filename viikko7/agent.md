# Tehtävä 5 agent mode


## Päätyikö agentti toimivaan ratkaisuun?
Agentti tuotti toimivan ratkaisun, mutta sovelluksen ulkoasu ja koodikannan rakenne ei ollut kovinkaan korkealaatuinen. 

## Miten varmistuit, että ratkaisu toimii?
Pyysin agenttia käynnistämään sovelluksen ja tein tutkivaa testausta. Ensimmäisellä käynnistyskerralla sovellus kaatui heti annettuani syötteenä "k", "s" tai "p". Bugi liittyi jotenkin jinja templattien yhteensopimattomuudesta enumerate -funktion kanssa. Huomautuksen jälkeen agentti sai ongelman korjattua ensimmäisellä yrityksellä.

Ajoin myös agentin generoimat testit ja ne menivät läpi. Testejä ei tosin ollut kovin monta.

Ensivaikutelma oli siis lupaava. Sovellus vaikutti toimivan peruskäytössä ja testitkin menivät läpi. Seuraavaksi tutkin ohjelmakoodia ja en löytänyt sieltä suurempia virheitä. 


## Oletko ihan varma, että ratkaisu toimii oikein?
En voi sanoa olevani täysin varma siitä etteikö koodissa olisi jotain ongelmia, joita en huomannut koodia katselmoidessani. Tekoälyn tuottama koodi vaikutti kaiken kaikkiaan järkevältä, mutta voi olla etten vain huomannut kaikkia ongelmakohtia.


## Kuinka paljon jouduit antamaan agentille komentoja matkan varrella?
Agentti yritti aluksi käyttää pip:iä muun muassa flaskin asentamiseen, vaikka olin ohjeistanut sitä käyttämään poetryä. Parin jatkokehoituksen jälkeen agentti sai sovelluksen käynnistettyjä.

Agentti totettu koko sovelluksen yhdessä tiedostossa, mukaan lukien jinja template. Pyysin agenttia parantamaan projektin tiedostorakennetta luomalla muun muassa templates kansion.



## Kuinka hyvät agentit tekemät testit olivat?
Yksittäiset testit vaikuttivat hyviltä, mutta testitapauksia olisi voinut olla enemmän. 


## Onko agentin tekemä koodi ymmärrettävää?
Koodi on suurimmaksi osaksi ymmärrettävää muutaman refaktorointipyynnön jälkeen. Tekoälyn luomissa tiedostoissa on monia koodirivejä, joita tekoäly vaikutti tarvitsevan tiedostopolun määrittämiseen. Sovelluksen rakennetta voisi edelleen parantaa.


## Miten agentti on muuttanut edellisessä tehtässä tekemääsi koodia?
Agentti ei juuri muokannut luomaani koodia.


## Mitä uutta opit?
Agent moden käyttö IDE:n kautta tuli tutuksi, sillä en ollut aikaisemmin käyttänyt sitä vs codessa. 

