# entity engine
# note: pprint is for pretty print

import phylo
import event
import phylo_dic
import event_dic
import home
from random import shuffle

class Entity(object):
    class Deck(object):
        def __init__(self, pdeck, phci):
            self.cont = []            # @below: get home card its own class in an Entity?
            self.hc = home.Home(phci) # is initing with strings such a good idea? idk.
            for a_card_name in pdeck:
                if phylo_dic.get(a_card_name):
                    self.cont.append(phylo.Phylo(a_card_name))
                if event_dic.get(a_card_name): # in case there are terrain cards or stuff to implement
                    self.cont.append(event.Event(a_card_name))
            
        def get_cont(self):
            return self.cont
            
        def get_size(self):
            return len(self.cont)    
            
        def append(self, pl):
            self.cont.append(pl)
    
        def shuffle(self):
            shuffle(self.cont)
            
        def pop(self, pnum):
            if 0 <= pnum < self.get_size():
                return self.cont.pop(pnum)
            else:
                return False
            
        def get_home_card(self):
            return self.hc
    
    
    
    
    class Hand(object):
        def __init__(self):
            self.cont = []
            
        def get_cont(self):
            return self.cont
            
        def get_size(self):
            return len(self.cont)    
            
        def draw(self, pl):
            self.cont.append(pl)

        def pop(self, pnum):
            if 0 <= pnum < self.get_size():
                return self.cont.pop(pnum)
            else:
                return False
                
        def shuffle(self):
            shuffle(self.cont)
            
        def append(self, lcard):
            self.cont.append(lcard)
            
        def pprint(self):
            for i in range(self.get_size()):
                print "%d: %s" % (i, self.cont[i].get_name())
            
        def pprint2(self):
            for cd in self.cont:
                print cd.get_name()
                
                                        
            
            
    class Discard_Pile(object):
        def __init__(self):
            self.cont = []
        
        def get_size(self):
            return len(self.cont)
            
        def lay(self, lcard):
            self.cont.append(lcard)
                            
            
                
    
    def __init__(self, pinfo, pdeck, phci, ptype):
        self.name = pinfo
        self.deck = Entity.Deck(pdeck, phci) # < This is the "cache deck". The immutable version
        #if self.get_cards_left() < 19: raise SystemExit # error catching my style
        self.moves_left = 0                  # is found in what's currently the pylo.main().
        self.type = ptype # 0: human # 1: dumb AI
        self.hand = Entity.Hand()
        self.disc_pile = Entity.Discard_Pile()
        
    def get_cards_left(self):
        return self.deck.get_size()
        
    def get_cards_in_hand(self):
        return self.hand.get_size()
        
    def get_cards_in_deck(self): # a duplicate
        return self.deck.get_size()
    
    def get_type(self):
        return self.type    
        
    def get_name(self):
        return self.name
        
    def get_deck(self):
        return self.deck
        
    def get_hand(self):
        return self.hand
        
    def get_moves_left(self):
        return self.moves_left
        
    def set_moves_left(self, pnum):
        self.moves_left = pnum
     
    def moves_left_equals_minus_one(self):
        self.moves_left -= 1
        
    def draw(self, how_many):
        for i in range(how_many):
            lcard = self.deck.pop(0)
            self.hand.append(lcard)

    def discard(self, pinhand):
        lcard = self.hand.pop(pinhand)
        if lcard:
            self.disc_pile.lay(lcard)
            return lcard
