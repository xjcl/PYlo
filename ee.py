# entity engine
import phylo
import event
import phylo_dic
import event_dic
from random import shuffle

class Entity(object):
    def __init__(self, pinfo, pdeck): # deck as list of (common) names
        self.name = pinfo
        self.deck = []
        self.moves_left = 0
        for a_card_name in pdeck:
            if phylo_dic.get(a_card_name):
                self.deck.append(phylo.Phylo(a_card_name))
            if event_dic.get(a_card_name): # in case there are terrain cards or stuff
                self.deck.append(event.Event(a_card_name))
        
    def get_name(self):
        return self.name
        
    def get_deck(self):
        return self.deck
        
    def shuffle_deck(self): # um... own deck class?
        shuffle(self.deck)
        
    def get_moves_left(self):
        return self.moves_left
        
    def set_moves_left(self, pnum):
        self.moves_left = pnum
     
    def moves_left_equals_minus_one(self):
        self.moves_left -= 1
