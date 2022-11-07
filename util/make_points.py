elements = ["Air", "Fire", "Earth", "Water"]

i = 39
sym = 128769

for point in elements:
    print({"model": "faq.astropoint", "pk": i, "fields": {"name": point, "description": "", "symbol": str(sym), "tag": "element"}})
    i = i + 1
    sym = sym + 1


