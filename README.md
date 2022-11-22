# Asteroids peliprojekti

### Huomio Python-versiosta
Pelin toiminta on testattu Python-versiolla 3.8

### Dokumentaatio
- [Vaatimusmäärittely](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/changelog.md)

## Pelin asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

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

