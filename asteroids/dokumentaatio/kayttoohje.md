# Käyttöohje
Asteroids project on mukaelma retropelistä Asteroids. Pelin tarkoituksena on lennellä satunnaisesti muuttuvassa asteroidivyöhykkeessä ja yrittää selviytyä mahdollisimman pitkään hengissä. Törmäykset asteroidien kansssa vähentävät aluksen energiaa ja kolmas törmäys tuhoaa aluksen. Pelaaja voi tuhota asteroideja ampumalla niitä.

## Ohjelman asentaminen ja käynnistäminen
1. Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.
2. Pura lataamasi .zip/.tar.gz-tiedoston sisältö valitsemaasi hakemistoon
3. Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

4. Jonka jälkeen ohjelman voi käynnistää komennolla:
```bash
poetry run invoke start
```
## Muut komentorivikäskyt
### Lähdekoodin muotoilu
Lähdekoodin PEP-8-tyyliohjeen mukaisen muotoilun voi suorittaa komennolla:
```bash
poetry run invoke format
```
### Pylint
Koodin laatua voi arvioida suorittamalla kommmennon:
```bash
poetry run invoke lint
```
### Koodin testaus
Ohjelmakoodin valmiit testit voi ajaa suorittamalla komennon:
```bash
poetry run invoke test
```
Koodin testikattavuusraportin voi suorittaa komennolla:
```bash
poetry run invoke coverage-report
```
Raportti luodaan htmlcov kansioon.

## Uuden pelin käynnistäminen
Sovellus käynnistyy päävalikkoon:

![image](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kuvat/newgame.png)

Valikoissa liikutaan nuolinäppäimillä ylös ja alas, valinnat tehdään painamalla Enter.

Päävalikosta on mahdollista siirtyä uuteen peliin valitsemalla "New Game". Lisäksi on mahdollista tarkastella parhaita pisteitä valitsemalla "High Scores" tai katsoa ohjeet valitsemalla "Controls". Pelin voi lopettaa valitsemlla "Exit"

## Pelaaminen
Peliä pelataan näppäimistöllä. Seuraavassa on käytettävissä olevat näppäimet:
- Vasen/oikea: käännä alusta vasemmalle / oikealle
- Ylös: Kiihdytä aluksen vauhtia
- Välilyönti: Laukaise ammus aluksen osoittamaan suuntaan
- Esc: pysäytä peli ja hengähdä pysäytysvalikossa
- m: pysäytä musiikki
- n: pysäytä tehosteäänet
![image](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kuvat/controls.png)

### Nimen/nimimerkin syöttäminen pelin päättyessä
Pelaaja saa syöttää nimensä pelin päätyttyä. Nimi/nimimerkki voi olla 1-20 merkkiä pitkä. Parhaat kymmenen pelaajaa ansaitsevat paikkansa High Scores näkymässä.
![image](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kuvat/insertname.png)


## Hauskoja pelihetkiä!
