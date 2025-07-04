from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time
import random
import os
import sys

INPUT = "sanat.txt"
OUTPUT = "uudet_sanat.txt"
INDEKSI_TIEDOSTO = "viimeinen_indeksi.txt"

# Merkinnät, joiden esiintyessä sana hylätään
EPAVIRALLISET_TERMIT = [
    "ark.", "puhek.", "murt.", "slg.", "last.",
    "leik.", "halv.", "alat.", "ylät.", "vanh."
]

def onko_yleiskielinen(sana, driver):
    url = f"https://www.kielitoimistonsanakirja.fi/#/{sana}"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "definition"))
        )
    except Exception:
        with open("viimeinen_virhesivu.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("\n❌ DOM ei ilmestynyt. Tallennetaan indeksi ja pysäytetään.")
        raise RuntimeError("DOM ei ilmestynyt")

    # Haetaan ensimmäinen määritelmä (definition)
    try:
        eka_def_elem = driver.find_element(By.CLASS_NAME, "definition")
        eka_def_text = eka_def_elem.text.lower()
    except:
        eka_def_text = ""

    # Haetaan heti seuraava elementti (yleensä tyyli/sanaluokka)
    try:
        seuraava = eka_def_elem.find_element(By.XPATH, "following-sibling::*[1]").text.lower()
    except:
        seuraava = ""

    # Yhdistetään molemmat tarkastelua varten
    teksti = eka_def_text + "\n" + seuraava

    for termi in EPAVIRALLISET_TERMIT:
        if termi in teksti:
            return False, termi

    sleep(random.uniform(0.01, 0.02))
    return True, ""

def prosessoi(jatka_vain):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)

    with open(INPUT, encoding="utf-8") as f:
        rivit = [r.strip() for r in f if r.strip()]

    print(f"\nLuettiin {len(rivit)} tavutettua sanaa tiedostosta {INPUT}.\n")

    aloitusindeksi = 1
    if jatka_vain and os.path.exists(INDEKSI_TIEDOSTO):
        with open(INDEKSI_TIEDOSTO, encoding="utf-8") as f:
            try:
                aloitusindeksi = int(f.read().strip())
            except:
                pass

    kokonaismaara = len(rivit)
    start_time = time()

    for i in range(aloitusindeksi - 1, len(rivit)):
        tavutettu = rivit[i]
        sana = tavutettu.replace("-", "")
        tehty = i + 1
        print(f"[{tehty}/{kokonaismaara}] {sana}...", end=" ")

        try:
            ok, syy = onko_yleiskielinen(sana, driver)
        except Exception as e:
            print(f"\n❌ Keskeytetään. Virhe sanassa '{sana}': {e}")
            with open(INDEKSI_TIEDOSTO, "w", encoding="utf-8") as f:
                f.write(str(tehty))
            driver.quit()
            raise

        if ok:
            print("✅ OK")
            with open(OUTPUT, "a", encoding="utf-8") as f:
                f.write(tavutettu + "\n")
        else:
            print(f"❌ hylätty ({syy})")

        with open(INDEKSI_TIEDOSTO, "w", encoding="utf-8") as f:
            f.write(str(tehty + 1))

        # Aika-arvio
        kulunut = time() - start_time
        tehty_maara = tehty - (aloitusindeksi - 1)
        arvio_jaljella = (kokonaismaara - tehty) * (kulunut / tehty_maara)
        minuutit = int(arvio_jaljella // 60)
        sekunnit = int(arvio_jaljella % 60)
        print(f"(arvio jäljellä: {minuutit} min {sekunnit} s)")

        if tehty_maara % 20 == 0:
            print("\n🕓 Pidetään pieni tauko bottisuojan välttämiseksi ( 0.1sekuntia)...\n")
            sleep(0.1)

    driver.quit()
    print(f"\nValmis. Viimeinen indeksi kirjattu tiedostoon {INDEKSI_TIEDOSTO}.")

if __name__ == "__main__":
    jatka = "--jatka" in sys.argv
    prosessoi(jatka_vain=jatka)
