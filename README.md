# Varjosää

Läpinäkyvä neoninsininen wttr.in-sääwidget Linuxille ja Androidille. Näyttää kolmen päivän ennusteen: alin ja ylin lämpötila, keskipäivän säätila ja suurin päivän sateen todennäköisyys. Ennuste alkaa tästä päivästä.

## Linux

Lataa julkaisun Varjosaa-0.1.0-x86_64.AppImage, anna suoritusoikeus ja käynnistä. PyQt6 on paketissa mukana. Hiiren oikea painike tai kaksoisnapsautus avaa asetukset. Widgetiä voi vetää tekstistä. Asetuksista voit säätää fonttia, tekstikokoa, väriä, peittävyyttä, sijaintilukitusta ja valinnaista kelloa/päivämäärää. Waylandissa sijoittelua hallitsee myös ikkunointijärjestelmä.

Sijainti voidaan hakea automaattisesti julkisesta IP-osoitteesta tai kirjoittaa kaupungin/kylän nimi (tarvittaessa maa). IP-sijainti voi olla VPN:n tai operaattorin sijainti, ei GPS. Paikkakunta lähetetään HTTPS-yhteydellä wttr.in-palveluun. Sää haetaan taustalla tunnin välein, ja viimeisin ennuste säilytetään paikallisesti yhteyskatkojen varalta. Menneitä ennustepäiviä ei näytetä.

Automaattikäynnistykseen voi lisätä AppImagen GNOME:n käynnistyviin ohjelmiin tai luoda ~/.config/autostart/varjosaa.desktop-tiedoston:

```ini
[Desktop Entry]
Type=Application
Name=Varjosää
Exec=/täysi/polku/Varjosaa-0.1.0-x86_64.AppImage
Terminal=false
X-GNOME-Autostart-enabled=true
```

Lähdekoodista: `python3 -m venv .venv`, `.venv/bin/pip install -r requirements.txt`, `.venv/bin/python main.py`.

## Android

Android 6.0 tai uudempi (API 23), natiivi kotinäyttöwidget. Asenna test-APK ja lisää Varjosää kotinäytön Widgetit-valikosta. Napautus avaa asetukset. Kasvata widgetin korkeutta, jotta ennuste mahtuu. Päivitys käyttää verkkoyhteyttä ja JobScheduleria; Androidin virransäästö voi viivästyttää sitä. Ei GPS-oikeuksia. APK on debug-allekirjoitettu testiversio: tulevien testiversioiden allekirjoitus voi muuttua ja asennus edellyttää aiemman testiversion poistamista. Fyysistä Android-laitetestausta ei ole tehty.

## Kehitys ja lisenssit

`python3 -m unittest discover -s tests -v` ja `QT_QPA_PLATFORM=offscreen python3 main.py --self-test`. Julkaisun GitHub Actions rakentaa ja tarkistaa AppImagen sekä test-APK:n. Lähdekoodi MIT (Jakke77). PyQt6:n ja muiden mukana toimitettujen riippuvuuksien omat lisenssit ovat voimassa; katso THIRD_PARTY_NOTICES.md. Säädata ja palvelu: [wttr.in](https://github.com/chubin/wttr.in). Erillinen Varjoaika-kalenteri: [goottikalenteri](https://github.com/Jakke77/goottikalenteri).
