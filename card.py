class Card(object):
    def __init__(self, pcontent, ptype):
        self.content = pcontent
        self.type = ptype
    
    def get_content(self):
        return self.content
        
    def get_type(self):
        return self.type
