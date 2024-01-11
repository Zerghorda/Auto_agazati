class Auto:
    def __init__(self, sor: str):
        sorok = sor.strip().split("$")
        self.nev = sorok[0]
        self.datum = int(sorok[1])

    def __str__(self):
        return f"nev:{self.nev},datum:{self.datum}"


