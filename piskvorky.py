import ai
def vyhodnot(hraci_pole):
    if 'xxx' in hraci_pole:
        return 'x'
    elif 'ooo' in hraci_pole:
        return 'o'
    elif '-' not in hraci_pole:
        return '!'
    else:
        return '-'


def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    nove_pole = pole[:cislo_policka] + symbol + pole[(cislo_policka + 1):]
    return nove_pole


def tah_hrace(pole):
    while True:
        pozice = int(input('Zadej pozici: '))
        if pozice < 0 or pozice > 19:
            print('Pozice je mimo rozsah.')
        else:
            if pole[pozice] != '-':
                print('Pozice je obsazena.')
            else:
                nove_pole = tah(pole, pozice, 'o');
                return nove_pole
