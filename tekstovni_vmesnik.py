#Tekstovni vmesnik
import model

prehod = '___________________________________'

def izpis_zmaga(igra):
    '''Če kdo zmaga'''
    igra.naslednji()
    tekst = prehod + '\n \n Zmagal je {}'.format(igra.navrsti)
    print(tekst)
    return

def natisni_mreza(igra):
    '''Natisne mrežo'''
    sez  = igra.mreza[::-1]
    for mreza in sez:
        print(mreza)
    return

def kam():
    '''Vpraša v katero mrežo bo igral'''
    return input("V katero mrežo boste igrali: ")

def vmesnik():
    igra_1 = model.igra()
    while True:
        natisni_mreza(igra_1)
        if igra_1.stiri_v_vrsto():
            izpis_zmaga(igra_1)
            input("?")
            return
        else:
            print("Na potezi je {}".format(igra_1.navrsti))
            stolpec = int(kam())
            igra_1.poteza(stolpec)
    return

vmesnik()


# igra_1 = model.igra()
# for i in range(3):
#     igra_1.kam(i)
#     igra_1.kam(i)
# igra_1.kam(3)
# natisni_mreza(igra_1)
# print(igra_1.stiri_v_vrsto())
# izpis_zmaga(igra_1)