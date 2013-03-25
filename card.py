class Card(object):
    def __init__(self, pcontent):
        self.content = pcontent
    
    def get_content(self):
        return self.content
        
    def get_cont(self):
        return self.get_content()
        
    def get_type(self):
        return self.content.get_type()
        
    def update(self):
        if self.get_type() == "Event":
            self.content.update() # < currently dead code
