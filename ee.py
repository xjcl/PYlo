# entity engine
import phylo
import event
import phylo_dic
import event_dic
import home
from random import shuffle

class Entity(object):
    class Deck(object):
        def __init__(self, acont, phci):
            self.cont = acont
            self.hc = home.Home(phci) # is initing with strings such a good idea? idk.
            
        def get_size(self):
            return len(self.cont)    
            
        def append(self, pl):
            self.cont.append(pl)
    
        def shuffle(self): # um... own deck class?
            shuffle(self.deck)
            
        def get_home_card(self):
            return self.hc
    
    
    
    def __init__(self, pinfo, pdeck, phci, ptype):
        self.name = pinfo
        self.deck = Entity.Deck(pdeck, phci)
        self.moves_left = 0
        self.type = ptype # 0: human # 1: dumb AI
        for a_card_name in pdeck:
            if phylo_dic.get(a_card_name):
                self.deck.append(phylo.Phylo(a_card_name))
            if event_dic.get(a_card_name): # in case there are terrain cards or stuff
                self.deck.append(event.Event(a_card_name))
    
    def get_type(self):
        return self.type    
        
    def get_name(self):
        return self.name
        
    def get_deck(self):
        return self.deck
        
    def get_moves_left(self):
        return self.moves_left
        
    def set_moves_left(self, pnum):
        self.moves_left = pnum
     
    def moves_left_equals_minus_one(self):
        self.moves_left -= 1
