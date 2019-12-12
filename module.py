#stiri v vrsto

class igra:
    def __init__(self, poteza, mreza = None):
        self.poteza = 'O'

        if mreza is None: 
            self.mreza = [['-','-','-','-','-','-', '-'] for _ in range(6)]
        else: 
            self.mreza = mreza

        def stiri_v_vrsto(self):
            '''Preveri, če so kje v mrezi 4 v vrsto'''
            pass

        def visina(self, stolpec):
            '''Katera vrsta v določenem stolpcu je prazna'''
            pass

        def poteza(self, stolpec):
            '''Naredi potezo'''
            pass