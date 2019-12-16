#stiri v vrsto

class igra:
    def __init__(self, mreza = None):
        self.navrsti = 'O'
        self.zadnja_poteza = (0,0) #(visina, stolpec)

        if mreza is None: 
            self.mreza = [['-','-','-','-','-','-', '-'] for _ in range(6)] #seznami so narobe obrnjeni od vzgoraj navzdol je za igrt
        else: 
            self.mreza = mreza

    def stiri_linija_seznami(self):
        '''Vrne vse sezname v katerih je lahko 4 v vrsto'''
        sez_r_diagonala = []
        sez_p_diagonala = []
        sez_visina = []
        for i in range(-3,4):
            if (6 > self.zadnja_poteza[0] + i >= 0) and (7 > self.zadnja_poteza[1] + i >= 0) :
                sez_r_diagonala.append(self.mreza[self.zadnja_poteza[0] + i ][self.zadnja_poteza[1] + i ])
            else: pass
            if (6 > self.zadnja_poteza[0] + i >= 0) and (7 > self.zadnja_poteza[1] - i >= 0) :
                sez_p_diagonala.append(self.mreza[self.zadnja_poteza[0] + i ][self.zadnja_poteza[1] - i ])
            else: pass
            if (6 > self.zadnja_poteza[0] - i >= 0) and (7 > self.zadnja_poteza[1] + i >= 0) :
                sez_visina.append(self.mreza[self.zadnja_poteza[0] - i ][self.zadnja_poteza[1]])
            else: pass

        return [sez_r_diagonala, sez_p_diagonala, sez_visina, self.mreza[self.zadnja_poteza[0]]]

    def sez_str(self, sez):
        '''Preveri, če je v sez določen string'''
        for pod_sez in sez:
            if len(pod_sez) <= 3:
                pass
            else: 
                for i in range(len(pod_sez)):
                    try:
                        preveri = pod_sez[0 + i : 4 + i]
                        if preveri[0] == preveri[1] == preveri[2] == preveri[3] != '-' :
                            return True
                        else: pass
                    except IndexError: pass
        return False

    def stiri_v_vrsto(self): 
        '''Preveri, če so kje v mrezi 4 v vrsto'''
        return self.sez_str(self.stiri_linija_seznami())

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
# for i in range(4):
#     igra.poteza(i)
#     igra.poteza(i)
 
# for i in igra.mreza:
#     print(i)
# print(igra.zadnja_poteza)
# print(igra.navrsti)
# print(igra.stiri_linija_seznami())
# print(igra.sez_str(igra.stiri_linija_seznami()))
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