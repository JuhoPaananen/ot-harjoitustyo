# Asteroids peliprojekti
Toteutetaan ohjelmistotekniikan kurssin harjoitustyönä Asteroids pelin ideaa mukaileva peli Pygamella.

### Huomio Python-versiosta
Pelin toiminta on testattu Python-versiolla 3.8

### Dokumentaatio
- [Vaatimusmäärittely](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/changelog.md)
- [Testausdokumentti](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/testaus.md)

## Releases
- [Viikon 7 release - Loppupalautus](https://github.com/JuhoPaananen/ot-harjoitustyo/releases/tag/viikko7)
- [Viikon 6 release](https://github.com/JuhoPaananen/ot-harjoitustyo/releases/tag/viikko6)
- [Viikon 5 release](https://github.com/JuhoPaananen/ot-harjoitustyo/releases/tag/viikko5)

## Pelin asennus
1. Lataa pelin viimeisin versio ylhäältä kohdasta **Releases**
2. Pura lataamasi .zip/.tar.gz.
3. Asenna riippuvuudet komennolla:

```bash
poetry install
```

4. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Pelin suorittaminen

Pelin pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
### Huomio! Pelin musiikki
Pelin taustalla soi Kidd2Will - Fire Aura, joka on luultavasti tekijänoikeuden alainen kappale. Tämän kouluprojektin tarkoituksena ei ole rikkoa kyseistä tekijänoikeutta, vaan harjoitella toimivan pelin luomista musiikkeineen.
