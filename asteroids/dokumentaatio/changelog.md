# Changelog

## Viikko 3

- Peli-ikkuna aukeaa
- Peli-ikkunalle on asetettu avaruusaiheinen taustakuva
- Sovellus alustaa aluksen
- Testattu, että aluksen luokka on alustuksen jälkeen oikea
- Alus liikkuu peli-ikkunassa ja pysyy ikkunan rajojen sisällä

## Viikko 4

- Sovelluslogiikka erotettu käyttöliittymästä - testaaminen helpottui
- Testattu, että peli alustuu oikein ja alus pysyy rajojen sisällä
- Alusta pystyy nyt kiihdyttämään ja jarruttamaan
- Alustavat hahmotelmat aluksen ja suunnan vektoroinneista aloitettu

## Viikko 5

- Pelilogiikka rakennettu uudelleen Vector2 objektien päälle
- Peli pääelementeiltään valmis: pelaaja voi lentää ja ampua, asteroidit tuhoutuvat osumista ja asteroideja luodaan satunnaisesti, osumista lasketaan pisteitä ja peli päättyy elämien loppuessa (kolmesta törmäyksestä)
- Peliin on lisätty taustamusiikki ja äänitehosteet ampumiselle, asteroidin tuhoutumiselle ja törmäykselle
- Peliin tullaan lisäämään vielä tietokanta top-5 pisteitä varten sekä käyttöliittymä pelin sisäiseen liikkumiseen.

## Viikko 6
- Käyttöliittymää kehitetty edelleen ja luotu valikot ohjelman ajonaikaiselle navigoinnille. Placeholder parhaiden pisteiden esittämiseksi.
- Pelilogiikan eriyttämistä omaksi kokonaisuudeksi jatkettu irrottamalla äänienhallinta omaksi luokakseen (kiitos koodikatselmoinnin palautteenantajalle)
- Asteroidit hajoavat nyt pienemmiksi siten, että suurin hajoaa kahdeksi keskikokoiseksi ja keskikokoinen kahdeksi pieneksi.
- Testien lisääminen ja haaraumakattavuuden parantaminen. Testien kirjoittaminen helpottunut koodin kehittyessä.
- Musiikin ja tehosteäänet saa nyt pois päältä

## Viikko 7
- Lisätty pisteiden pysyväistallennus, joten pisteet voidaan nyt tallentaa ja niitä voidaan tarkastella pelissä
- Siirretty ampumismetodi ja ammustenhallinta Player-luokan vastuulle.
- Koodin siistimistä
- Lisätty valikkonäkymä näppäinohjeille
- Lisätty testejä ja laajenettu testikattavuutta
- Täydennetty dokumentaatiota
