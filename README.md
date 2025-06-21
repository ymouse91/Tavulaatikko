# Tavupeli – Sanaruudukko

**Tavupeli** on selainpohjainen suomenkielinen sanapeli, jossa pelaajan tehtävänä on järjestää tavuja ruudukkoon niin, että **jokainen vaakaan ja pystyyn muodostuva tavupari muodostaa oikean kaksitavuisen sanan**.

Peli toimii 3×3–5×5 ruudukossa ja on kehitetty HTML-, CSS- ja JavaScript-teknologioilla. Sovellus on asennettavissa myös mobiililaitteille (PWA).

---

## 🕹️ Peliohjeet

1. Valitse ruudukon koko (esim. 4×4).
2. Paina **"Aloita peli"**.
3. Ohjelma sekoittaa ruudukon tavut – yksi tavu paljastetaan oikealla paikallaan.
4. Klikkaa ensin yksi ruutu, sitten toinen vaihtaaksesi niiden paikkaa.
5. Jokainen **vierekkäinen tavupari** (vaaka- ja pystysuunta) tulee muodostaa **oikea sana**.
6. Kun koko ruudukko on oikein, peli ilmoittaa voitosta.
7. Voit koska tahansa:
   - Painaa **"Apua"** paljastaaksesi yhden oikean tavun (vihreä ruutu).
   - Painaa **"Lopeta – näytä ratkaisu"** nähdäksesi oikean ruudukon.

🔒 Vihreäksi paljastetut tavut lukitaan paikalleen.

---

## 🔁 Uuden pelin aloittaminen

Voit aloittaa uuden pelin valitsemalla koon ja painamalla "Aloita peli" uudelleen, kun edellinen peli on ratkaistu tai lopetettu.

---

## 🌐 Demo

➡️ [Pelaa verkossa GitHub Pagesissä](https://ymouse91.github.io/tavulaatikko/)

> Korvaa osoite omallasi

---

## 📦 Asennus paikallisesti

1. Lataa tai kloonaa repositorio:
   ```bash
   git clone https://github.com/käyttäjä/tavupeli.git
   ```
2. Avaa `index.html` selaimessa – toimii täysin ilman palvelinta.

---

## 📱 PWA (Progressive Web App)

Tavupeli on asennettavissa kotinäytölle:

- Lisää sovellus mobiiliselaimesta (esim. Chrome > Lisää aloitusnäyttöön)
- Toimii offline-tilassa (service worker + välimuisti)
- Käyttää `manifest.json` ja `service-worker.js`

---

## 🧾 Lisenssi

Käyttö sallittu opetuskäytössä ja henkilökohtaisiin projekteihin. Voit vapaasti muokata ja jakaa omasi.
