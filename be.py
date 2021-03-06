# FUN FACT: While trying to upload this to git in order not to lose any important files anymore,
# I lost the battle engine and had to rewrite it. This is the rewritten one.

# battle engine
from random import choice
import fe
import me

class Battle(object):
    def __init__(self, aplayers, story_mode):
        self.players = aplayers
        self.is_story = story_mode
        self.is_done = False
        self.round = 0
        lhcards = []
        for ply in aplayers:
            lhcards.append(ply.get_deck().get_home_card())
        self.fld = fe.Field(lhcards)
    
    def is_in_round(self):
        return self.round
        
    def next_round(self):
        self.round += 1
        
    def update(self):
        for a_row in self.fld.data:
            for a_stack in a_row:
                a_stack.update()
        
    def is_story(self):
        return self.is_story  
        
    def get_field(self):
        return self.fld  

    def get_number_of_players(self):
        return len(self.players)  

    def get_cards_in_hands(self):
        la = []
        for ply in self.players:
            la.append(ply.get_cards_in_hand())
        return la

    def get_cards_in_decks(self):
        la = []
        for ply in self.players:
            la.append(ply.get_cards_in_deck())
        return la
        
    def get_number_of_players(self):
        return len(self.players) 
                
    def run(self):
        if self.is_story and self.get_number_of_players() == 2:
            print "%s would like to battle!" % self.players[1].get_name()
        else:
            pass # TODO
        for ply in self.players:
            ply.get_deck().shuffle()
            ply.draw(5) # FIXME # error catching here if I have time # or check deck at init
        while self.is_done == False:
            for ply in self.players:
                ply.set_moves_left(3)
                print "\n"
                while ply.get_moves_left():
                
                    if ply.get_type() == 0:
                        npt_txt = raw_input("--> ")
                    elif ply.get_type() == 1:
                        npt_txt = choice(["pass", "d 0", "l 0 0 2", "l 0 2 3", "l 0 1 0", "l 0 3 2"]) # hehe # TODO AI module
                        
                    if me.npt(self, ply, npt_txt) == True: # False if command is a bunch of malarki
                        ply.moves_left_equals_minus_one()
                    print "%s has %d moves left.\n" % (ply.get_name(), ply.get_moves_left())
                    
            self.update()
            self.next_round()
