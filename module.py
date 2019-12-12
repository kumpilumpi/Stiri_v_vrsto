#stiri v vrsto

class igra:
    def __init__(self, mreza = None):
        self.navrsti = 'O'

        if mreza is None: 
            self.mreza = [['-','-','-','-','-','-', '-'] for _ in range(6)]
        else: 
            self.mreza = mreza

    def stiri_v_vrsto(self): #Mogoče dodam zadnja poteza var,da je mnj za pregledovt, če je konc
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
        self.mreza[self.visina(stolpec)][stolpec] = self.navrsti
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