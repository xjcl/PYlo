# field engine and
# square engine

class Field(object):
    def __init__(self, home1, home2):
        self.h1 = home1
        self.h2 = home2
        self.f = \
        [[Square(self, 0, 0, None), Square(self, 0, 1, None),\
        Square(self, 0, 2, None), Square(self, 0, 3, None)], \
        \
        [Square(self, 1, 0, None), Square(self, 1, 1, home.Home()),\
        Square(self, 1, 2, home.Home()), Square(self, 1, 3, None)],
        \
        [Square(self, 2, 0, None), Square(self, 2, 1, None),\
        Square(self, 2, 2, None), Square(self, 2, 3, None)]]
        
    #def check_move(self, move):
    
    
    def get_square(self, py, px):
        return self.f[py][px]
    
    def handle_lay(self, py, px, pcard):
        # don exits?
        if 0 <= py < len(self.f) and 0 <= px < len(self.f[0]): # FIXME # is_number()
            lsquare = self.get_square(py, px)
            if pp.get_type() == "Phylo":
                if lsquare.has_None(): # if None / empty
                    lsquare.lay_on_top(pp)
    
    #def handle_move(self, pstr):
        
