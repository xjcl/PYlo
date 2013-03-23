# battle engine
import ee
from shlex import split
import random
import me
import se

class Battle(object):
    def __init__(self, pp1, pp2): # are entities
        self.p1 = pp1
        self.p2 = pp2
        self.done = False
        
    def say_hi(self):
        print
        print "-----------------------------------------------"
        print "%s would like to battle!!" % self.p2.get_name()
        
    def do_init(self):
        self.say_hi()
        # put home card etc.
        
    def npt(self, player, pcmd):
        me.npt(player, pcmd)
        
    def update(self):
        for sq in the_field:
            sq.update()
        # count things down
        # check for compatibility
        # do rain etc. if implemented
        # oh and card effects
        # no wait I didn't want these
        
    def run(self):
        self.do_init()
        while not self.done:
            #self.update() # put to the end? (after p2 npt?)
            p1in = raw_input("\n\nYour turn.\n--> ")
            if p1in == "e":
                break
            elif p1in == "i":
                for p in self.p1.get_deck():
                    print p.get_dic()
            else:
                self.npt(self.p1, p1in)
                self.npt(self.p2, "grow 0") # random.choice(["u", "d", "l", "r"])
