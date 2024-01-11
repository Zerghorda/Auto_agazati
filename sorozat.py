import random

szamok = []
def fel2():
    print("II/A,B,C:")
    for i in range(5):
        szam = random.randint(1, 100)
        if i == 4:
            print(f"{szam}")
        else:
            print(f"{szam};", end="")
        szamok.append(szam)


def egyjegyuek_szama():
    egyjegyu: int = 0
    for i in szamok:
        if i < 10:
            egyjegyu += 1
    return egyjegyu


def konzol_kiir():
    szoveg: str = ""
    szoveg += "II/D,E:\n"
    szoveg += f"\tAz egyjegyűek száma : {egyjegyuek_szama()}"
    print(szoveg)
    return szoveg


def file_kiir():
    falj = open("szamok.txt", "w", encoding="utf-8")
    falj.write(konzol_kiir())
    falj.close()

