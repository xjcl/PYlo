# handles events
import event_dic

class Event(object): # contrary to its name, it is an event card
    def __init__(self, pname):
        self.dic = phylo_dic.get(pname) # self.dic curr only has one element in it # TODO
        
        self.name = pname
        self.index = self.dic
        # can be played on... phylo-type required or more? ... etc.
        # idea: check list of compatibles all the time, but make them "full"
        # if there are no further requirements
    
    
        
    def get_dic(self):
        return self.dic
        
    def get_name(self):
        return self.name
        
    def get_type(self):
        return "Event"
