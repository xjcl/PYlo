# field engine
from se import Square

class Field(object):
    def __init__(self, phomes):
        self.homes = phomes
        if len(self.homes) == 2: # len(self.homes) == number of players
            self.data = \
            [[Square(self, 0, 0, None), Square(self, 0, 1, None),\
            Square(self, 0, 2, None), Square(self, 0, 3, None)], \
            \
            [Square(self, 1, 0, None), Square(self, 1, 1, phomes[0]),\
            Square(self, 1, 2, phomes[1]), Square(self, 1, 3, None)],
            \
            [Square(self, 2, 0, None), Square(self, 2, 1, None),\
            Square(self, 2, 2, None), Square(self, 2, 3, None)]]
        
    #def check_move(self, move):
    
    
    def get_square(self, py, px):
        return self.data[py][px]
    
    def get_data(self):
        return self.data
    
    def lay(self, py, px, pcard):
        # don exits?
        if 0 <= py < len(self.data) and 0 <= px < len(self.data[0]): # FIXME # is_number()
            lsquare = self.get_square(py, px)
            if pcard.get_type() == "Phylo":
                if lsquare.has_None(): # if None / empty
                    lsquare.lay_on_top(pp)
    
    #def handle_move(self, pstr):
        
