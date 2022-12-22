# Testausdokumentti
Peliä on testattu Pythonin ´unittest' kirjaston avulla sekä erityisesti pelaajan syötteiden osalta manuaalisesti.

## Testit
Sovelluslogiikkasta vastaavaa ´AsteroidsGame´-luokkaa testataan ´TestAsteroidsGame´-luokalla. Tämän luokan testit kattavat myös useimmat 'utils'-työkalupaketin metodeista, koska testit synnyttävät monen luokan toiminnallisuuksia yhdistäviä ketjuja. 

Äänistä vastaavaa luokkaa 'Soundplayer' testataan 'TestSoundplayer' luokalla. Näissä testeissä pääroolissa on pygame.mixer tilan tarkistaminen eri metodien jälkeen.

Pelissä olevia objekteja testataan 'TestPlayer'- ja 'TestBullet'-luokilla. Asteroidit tulevat testattua varsin kattavasti 'TestAsteroidsGame'-luokan yhteydessä 'AsteroidsGame' ja 'Asteroids' luokkien useiden yhteyksien seurauksena.

Tietojen lukemista ja tallentamista testataan 'TestHighScoreRepository'-luokalla. Testejä varten käytössä on testi.csv, jotta tiedoston sisältö ei muutu peliä pelattaessa. Pelitapahtuman pisteiden tallentamista varten luodaan hetkellisesti uusi 'newfile.csv' tiedosto, joka poistetaan testien päätteeksi.

Käyttöliittymästä vastaavia menu-luokkia ei ole testattu ja pygamen pelaajan syötteille ei onnistuttu luomaan järkeviä testejä.

## Testauskattavuus
Käyttöliittymää lukuunottamatta pelin haaraumakattavuus on varsin hyvä 87%. Suurimmat testauspuutteet ovat 'AsteroidsGame'-luokassa, jonka testaaminen oli osin vaikeaa.

![image](https://github.com/JuhoPaananen/ot-harjoitustyo/blob/main/asteroids/dokumentaatio/kuvat/coverage_report.png)
