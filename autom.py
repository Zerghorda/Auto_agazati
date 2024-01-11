import Auto

f = open("auto.txt", "r", encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()


def flotta():
    db: int = len(sorok)
    print("III/Flotta:")
    print(f"\tAutók száma:{db}")


def legfiatallabb():
    print("III/Legfiatalabb:")
    legkissebb: int = 0
    neve: str = ""
    for i in range(len(sorok)):
        auto = Auto.Auto(sorok[i])
        if auto.datum > legkissebb:
            legkissebb = auto.datum
            neve = auto.nev
    print(f"\tA legfiatalabb autó: {neve} {legkissebb}")


def atlag_kor():
    print("III/Átlag kor:")
    osszeg: int = 0
    db: int = len(sorok)
    for i in range(len(sorok)):
        auto = Auto.Auto(sorok[i])
        osszeg += 2024 - auto.datum
    atlag: float = osszeg/db
    print(f"\tAz autók átlagos kora: {atlag:.2f} év.")


