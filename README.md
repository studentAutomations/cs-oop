# Web Scraper za Objektno-Orijentisano Programiranje

Ovaj projekat je **web scraper** koji automatski prati i beleži nove objave sa određenog sajta, a zatim obaveštava korisnike putem Discord aplikacije.

## Funkcionalnosti
- **Praćenje novih obaveštenja:** Program koristi Selenium za redovnu proveru sajta kako bi detektovao nove objave.
- **Čuvanje novosti:** Scrapovani sadržaj se automatski beleži i čuva u `.md` fajlu na ovom GitHub repozitorijumu.
- **Automatsko slikanje:** Generiše se screenshot relevantne objave.
- **Deljenje informacija:** Uz pomoć Discord webhook linka, slika i link ka novoj objavi šalju se korisnicima.
- **Automatizacija:** Koristi GitHub Actions za periodično pokretanje scrapper-a i ažuriranje podataka.

## Korišćene tehnologije
- **Selenium:** Za navigaciju i interakciju sa web stranicama.
- **GitHub Actions:** Za automatizaciju pokretanja scrapper-a i ažuriranje `.md` fajla.
- **Discord Webhook:** Za slanje obaveštenja korisnicima.
- **Kod iz forka:** Za čuvanje scrapovanih sadržaja u `.md` fajlu koristi se [git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action) koji je forkovan u [automatic-changes](https://github.com/studentAutomations/automatic-changes).

## Kako funkcioniše
1. **Periodično pokretanje:** GitHub Actions aktivira skriptu u unapred definisanim intervalima.
2. **Scraping:** Selenium pretražuje sajt i detektuje nove objave.
3. **Ažuriranje novosti:** Nove objave se dodaju u `.md` fajl u ovom repozitorijumu.
4. **Slanje obaveštenja:** Screenshot i link ka objavi šalju se putem Discord webhook-a svim korisnicima.

## Kako koristiti
1. Fork-ujte ovaj repozitorijum.
2. Dodajte svoj Discord webhook URL u konfiguraciju.
3. Aktivirajte GitHub Actions.
4. Pogledajte `.md` fajl za sačuvane novosti i pratite obaveštenja na Discord-u.

## Doprinos
Slobodno otvorite **issue** ili pošaljite **pull request** za predloge ili poboljšanja.

## Licence
[MIT Licence](./LICENSE)
