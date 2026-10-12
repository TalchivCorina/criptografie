# CIFRUL CEZAR - ALFABETUL ROMÂNESC

ALFABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
LATIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = len(ALFABET)
CHEIE_MIN = 1
CHEIE_MAX = N - 1
LUNGIME_MIN_CHEIE2 = 7


# returnează pozitia unei litere in alfabet
def pozitie_litera(c):
    try:
        return ALFABET.index(c.upper())
    except ValueError:
        return -1 #car. nu a fost gasit


# verifica daca o litera este latina A-Z
def este_latin(c):
    return c.upper() in LATIN


# pregateste textul,elimina spatiile,transforma in majuscule,verifica alfabetul romanesc

def pregateste_text(text):
    rezultat = ""

    for c in text:
        if c == " ":
            continue

        if pozitie_litera(c) == -1:
            raise ValueError(
                "Textul poate conține doar litere românești și spații."
            )

        rezultat += c.upper()

    if not rezultat:
        raise ValueError("Textul nu conține nicio literă.")

    return rezultat


# citeste o cheie numerică intre 1 si 30
def citeste_cheie():
    while True:
        try:
            cheie = int(input("Introdu cheia (1-30): "))

            if CHEIE_MIN <= cheie <= CHEIE_MAX:
                return cheie

            print("Cheia trebuie să fie între 1 și 30.")

        except ValueError:
            print("Introdu un număr întreg între 1 și 30.")


# citeste cheia 2, minimum 7 caractere ,numai litere latine
def citeste_cheie2():
    while True:
        cheie = input(
            "Introdu cheia 2 (minim 7 litere latine, fără diacritice): "
        )

        if len(cheie) < LUNGIME_MIN_CHEIE2:
            print("Cheia 2 trebuie să aibă cel puțin 7 litere.")
            continue

        if not all(este_latin(c) for c in cheie):
            print(
                "Cheia 2 trebuie să conțină doar litere latine "
                "(A-Z), fără diacritice."
            )
            continue

        return cheie.upper()


# construieste alfabetul de cifrare pentru varianta cu două chei
def construieste_alfabet(cheie2):
    alfabet_nou = ""

    # adaugam caracterele cheii fara repetari
    for c in cheie2:
        # transformam litera latina in pozitia corespunzatoare alfabetului romanesc
        litera = ALFABET[pozitie_litera(c)]

        if litera not in alfabet_nou:
            alfabet_nou += litera

    # adaugam restul alfabetului romanesc
    for c in ALFABET:
        if c not in alfabet_nou:
            alfabet_nou += c

    return alfabet_nou

# Criptare
def cripteaza(text, cheie, alfabet_cifrare):
    rezultat = ""

    for c in text:
        poz = pozitie_litera(c)
        rezultat += alfabet_cifrare[(poz + cheie) % N]

    return rezultat

# Decriptare
def decripteaza(text, cheie, alfabet_cifrare):
    rezultat = ""

    for c in text:
        poz = alfabet_cifrare.index(c)
        rezultat += ALFABET[(poz - cheie) % N]

    return rezultat

# citeste o alegere dintr-un interval
def citeste_optiune(mesaj, minim, maxim):
    while True:
        try:
            valoare = int(input(mesaj))

            if minim <= valoare <= maxim:
                return valoare

            print(f"Introdu o valoare între {minim} și {maxim}.")

        except ValueError:
            print(f"Introdu o valoare între {minim} și {maxim}.")

def main():

    while True:

        print("\nCIFRUL CEZAR ")
        print("1 - Cifrul Cezar cu o cheie")
        print("2 - Cifrul Cezar cu două chei")
        print("0 - Ieșire")

        metoda = citeste_optiune(
            "Alege varianta: ",
            0,
            2
        )

        if metoda == 0:
            print("Programul s-a încheiat.")
            break

        print("\n1 - Criptare")
        print("2 - Decriptare")

        operatie = citeste_optiune(
            "Alege operația: ",
            1,
            2
        )

        # cheia 1
        cheie = citeste_cheie()

        # Pentru o singura cheie folosim  alfabetul romanesc normal
        alfabet_cifrare = ALFABET

        # pentru doua chei construim alfabetul modificat
        if metoda == 2:
            cheie2 = citeste_cheie2()
            alfabet_cifrare = construieste_alfabet(cheie2)

            print("\nAlfabetul de cifrare:", alfabet_cifrare)

        # citirea textului
        text_citit = input(
            "\nIntrodu textul sau textul cifrat: "
        )

        try:
            text = pregateste_text(text_citit)

            if operatie == 1:
                rezultat = cripteaza(
                    text,
                    cheie,
                    alfabet_cifrare
                )
                print("\nCriptograma:", rezultat)

            else:
                rezultat = decripteaza(
                    text,
                    cheie,
                    alfabet_cifrare
                )
                print("\nMesajul decriptat:", rezultat)

        except ValueError as eroare:
            print("\nEroare:", eroare)

if __name__ == "__main__":
    main()
