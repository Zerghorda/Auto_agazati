def fel1():
    auto: str = input("Autó neve:")
    ev: int = int(input("Gyártás dátuma:"))
    print("I/A:")
    print(f"\tAutó neve : {auto}")
    print(f"\tGyártási dátum: {ev}")
    print("I/B:")
    if ev == 2024:
        print("\tfriss gyártás")
    elif ev <= 2000:
        print("\töreg autó")
    else:
        print("\tátlagos korú")



