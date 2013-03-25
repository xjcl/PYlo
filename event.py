# handles events
import event_dic

play_types = ["direct play", "on species", ""]

class Event(object): # contrary to its name, it is an event card
    def __init__(self, pname):
        self.dic = phylo_dic.get(pname) # self.dic curr only has one element in it # TODO
        self.square = None
        self.name = pname
        self.indexes = self.dic["indexes"]
        self.rl = self.dic["rl"] # rounds left
        for action_code in self.indexes:
            if action_code in [0]:
                self.play_type = 1
                break
        # can be played on... phylo-type required or more? ... etc.
        # idea: check list of compatibles all the time, but make them "full"
        # if there are no further requirements
    
    def decrease_rl(self):
        self.rl -= 1
        
    def check(self):
        if self.rl < 1:
            self.square.get_stack().pop()    
    
    def lay(self): # initial activation # TODO FIXME
        for action_codes in self.indexes:
            if action_code[0] == 0: # 0: discard species immediately
                if action_code[1] == 0: # 0 0: on ocean [salt water] or fresh water based cards
                    if 5 in self.square.get_phylo().get_terrain() or 6 in self.square.get_phylo().get_terrain():
                        self.square.pop_phylo()
        self.check()
                    
    def activate(self):
        pass                
                    
    def play(self, psquare, pa): # TODO FIXME
        self.square = psquare
        if self.play_type == 1:
            self.lay(pa)
            self.square.append(self)
        elif self.play_type == 0:
            self.activate()
              
    def set_stack(self, pstack):
        self.stack = pstack
        
    def get_dic(self):
        return self.dic
        
    def get_name(self):
        return self.name
        
    def get_type(self):
        return "Event"
