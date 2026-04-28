#def vypocet_vahy(vaha_na_zemi, teleso="mesic"):
    """
    Vypočítá váhu astronauta na jiném tělese.
    Měsíc: 16.5 % váhy na Zemi (0.165)
    Mars: 38 % váhy na Zemi (0.38)
    """

    # kontrola záporné hodnoty
    if vaha_na_zemi < 0:
        print("Varování: váha nemůže být záporná!")
        return 0

    if teleso == "mesic":
        vysledek = vaha_na_zemi * 0.165
    elif teleso == "mars":
        vysledek = vaha_na_zemi * 0.38
    else:
        vysledek = vaha_na_zemi

    return vysledek


def simulator_pristani():

    vyska = 100
    rychlost = 10
    palivo = 50
    gravitace = 2

    print("\n--- ZAČÍNÁ PŘISTÁVACÍ MANÉVR ---")

    while vyska > 0:
        print(f"Výška: {vyska}m | Rychlost: {rychlost}m/s | Palivo: {palivo}j")

        # vstup uživatele
        zazeh = int(input("Zadej zážeh (0-10): "))

        # omezení paliva
        if zazeh > palivo:
            zazeh = palivo

        palivo -= zazeh

        # fyzika
        rychlost += gravitace
        rychlost -= zazeh
        vyska -= rychlost

        print("-" * 20)

        if vyska <= 0:
            break

    print(f"\nDopadová rychlost: {rychlost} m/s")

    if rychlost < 5:
        print("Výsledek mise: ÚSPĚŠNÉ PŘISTÁNÍ")
    else:
        print("Výsledek mise: HAVÁRIE")


# === HLAVNÍ PROGRAM ===
moje_vaha = 80
print(f"Moje váha na Měsíci: {vypocet_vahy(moje_vaha, 'mesic')} kg")

# spuštění simulace
simulator_pristani()
