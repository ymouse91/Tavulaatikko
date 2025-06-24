with open("sallitut_sanat.txt", "r", encoding="utf-8") as f:
    rivit = set(r.strip() for r in f if "-" in r)

with open("sallitut_sanat.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(rivit)))
