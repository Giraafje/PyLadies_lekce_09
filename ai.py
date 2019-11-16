def tah_pocitace(pole):
    while True:
        pozice = randrange(0, 20)
        if pole[pozice] == '-':
        # pokud je pozice volna, proved tah
            nove_pole = tah(pole, pozice, 'x')
            return nove_pole
