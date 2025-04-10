# kellotuksem.me
Tietokannat ja web-ohjelmointi kurssin harjoitustyö

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

* Käyttäjä pystyy lisäämään sovellukseen kellotuksia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kellotuksia.

* Käyttäjä näkee sovellukseen lisätyt kellotukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kellotukset.

* Käyttäjä pystyy etsimään kellotuksia hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä tietokohteita.

* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja (kellotusten määrä, kellotuksiin kulunut yhteenlaskettu aika ja jotain muuta nippelitietoa (esim. käyttäjän juoduin juoma))

* Käyttäjä pystyy valitsemaan kellotukselle yhden tai useamman luokittelun. (aika, juoman tyyppi, juoman alkoholipitoisuus, juoman määrä, hiilihapot, arvostelu)

* Käyttäjät pystyvät vertailemaan kellotuksia toisten käyttäjien kellotuksiin tulostaulukon avulla (järjestystä voi muuttaa esim. ajan, juoman määrän ja alkoholipitoisuuden perusteella)

* Käyttäjä pystyy lisämään videon suorituksesta

* Käyttäjä voi saada erilaisia saavutuksia ja "arvonimiä", joita voi esitellä profiilissa

## Tällä hetkellä sovelluksessa olevat toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

* Käyttäjä pystyy lisäämään sovellukseen kellotuksia. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kellotuksia.

* Käyttäjä näkee sovellukseen lisätyt kellotukset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kellotukset.

* Käyttäjä pystyy etsimään kellotuksia hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä tietokohteita.

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

## Mikä ihmeen kellotus?
Kellotuksella tarkoitetaan juoman juomista yleensä mahdollisimman nopeasti samalla kun suorituksesta otetaan aikaa.
