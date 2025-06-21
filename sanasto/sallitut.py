from collections import Counter

with open("kaksitavuiset_sanat_kotus.txt", encoding="utf-8") as f:
    rivit = [r.strip() for r in f if "-" in r and not r.strip().endswith("-")]

t1t2 = [tuple(r.split("-", 1)) for r in rivit if "-" in r]
tavulista = [t for pari in t1t2 for t in pari]
laskuri = Counter(tavulista)

suodatetut = [f"{a}-{b}" for a, b in t1t2 if laskuri[a] > 1 and laskuri[b] > 1]

with open("sallitut_sanat.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(suodatetut))
