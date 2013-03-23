# handles phylomon
import event_dic

class Event(object): # contrary to its name, it is an event card
    def __init__(self, pname):
        self.dic = phylo_dic.get(pname) # self.dic curr only has one element in it # TODO
        
        self.index = self.dic
    
    
        
    def get_dic(self):
        return self.dic
