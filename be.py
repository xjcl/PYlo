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
        lhcards = []
        for ply in aplayers:
            lhcards.append(ply.get_deck().get_home_card())
        self.fld = fe.Field(lhcards)
        
    def update(self):
        for a_row in self.fld.data:
            for a_stack in a_row:
                a_stack.update()
        
    def is_story(self):
        return self.is_story    
        
    def run(self):
        if self.is_story:
            print "%s would like to battle!" % self.players[1].get_name()
        else:
            pass # TODO
        while self.is_done == False:
            for ply in self.players:
                ply.set_moves_left(3)
                while ply.get_moves_left():
                
                    if ply.get_type() == 0:
                        npt_txt = raw_input("--> ") # FIXME # TODO # count down!
                    elif ply.get_type() == 1:
                        npt_txt = choice(["pass"]) # hehe
                        
                    if npt_txt == "exit":
                        raise SystemExit
                    ply.moves_left_equals_minus_one()
                    me.npt(ply, npt_txt)
                    print "%s has %d moves left." % (ply.get_name(), ply.get_moves_left())
            self.update()
