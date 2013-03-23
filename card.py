class Card(object):
    def __init__(self, pcontent, ptype):
        self.content = pcontent
        self.type = ptype # "Phylo", "Event"
    
    def get_content(self):
        return self.content
        
    def get_type(self):
        return self.type
        
    def update(self):
        if self.type == "Event"
            self.content.update()
