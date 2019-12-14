#stiri v vrsto

class igra:
    def __init__(self, mreza = None):
        self.navrsti = 'O'
        self.zadnja_poteza = (0,0) #(visina, stolpec)

        if mreza is None: 
            self.mreza = [['-','-','-','-','-','-', '-'] for _ in range(6)] #seznami aso narobe obrnjeni od vzgoraj navzdol je za igrt
        else: 
            self.mreza = mreza

    def stiri_linija_seznami(self):
        '''Vrne vse sezname v katerih je lahko 4 v vrsto'''
        sez_r_diagonala = []
        sez_p_diagonala = []
        sez_visina = []
        for i in range(-3,4): #linija
            try:
                sez_r_diagonala.append(self.mreza[self.zadnja_poteza[0] + i ][self.zadnja_poteza[1] + i ])
            except: pass
            try:
                sez_p_diagonala.append(self.mreza[self.zadnja_poteza[0] - i ][self.zadnja_poteza[1] - i ])
            except: pass
            try:
                sez_visina.append(self.mreza[self.zadnja_poteza[0] - i ][self.zadnja_poteza[1]])
            except: pass

        return [sez_r_diagonala, sez_p_diagonala, sez_visina, self.mreza[self.zadnja_poteza[0]]]


    def stiri_v_vrsto(self): #Mogoče dodam zadnja poteza var,da je mnj za pregledovt, če je konc
        #Try: Except IndexError
        #dodatna spremenljivka seznam seznamov, v katerih preveri, če so notr 4 v vrsto
        '''Preveri, če so kje v mrezi 4 v vrsto'''
        pass

    def naslednji(self):
        '''Pove kdo je naslednji na vrsti'''
        return 'O' if self.navrsti == 'X' else 'X'

    def visina(self, stolpec): #dela
        '''Katera vrsta v določenem stolpcu je prazna'''
        for i in range(6):
            if self.mreza[i][stolpec] == '-':
                return i
        return False

    def poteza(self, stolpec):
        '''Naredi potezo'''
        self.zadnja_poteza = (self.visina(stolpec), stolpec)
        self.mreza[self.zadnja_poteza[0]][stolpec] = self.navrsti
        self.navrsti = self.naslednji()
        return

# igra = igra()
# print(igra.navrsti)
# print(igra.mreza)
# print(igra.visina(0))
# igra.poteza(3)
# print(igra.navrsti)
# print(igra.mreza)
# igra.poteza(3)
# print(igra.mreza)
# igra.poteza(3)
# igra.poteza(3)
# igra.poteza(3)
# print(igra.mreza)