## Käyttöohje
Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

### Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:
```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:
```bash
poetry run invoke start
```

### Käynnistäminen
Sovellus käynnistyy päävalikkoon:

![image](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kuvat/mainmenu.png)

Valikoissa liikutaan nuolinäppäimillä ylös ja alas, valinnat tehdään painamalla Enter.

Päävalikosta on mahdollista siirtyä uuteen peliin valitsemalla "New Game". Lisäksi on mahdollista tarkastella parhaita pisteitä valitsemalla "High Scores" tai katsoa ohjeet valitsemalla "Help". Pelin voi lopettaa valitsemlla "Exit"

### Pelaaminen
Peliä pelataan näppäimistöllä. Seuraavassa on käytettävissä olevat näppäimet:
- Vasen/oikea: käännä alusta vasemmalle / oikealle
- Ylös: Kiihdytä aluksen vauhtia
- Välilyönti: Laukaise ammus aluksen osoittamaan suuntaan
- Esc: pysäytä peli
- m: pysäytä musiikki
- n: pysäytä tehosteäänet
