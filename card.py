class Card(object):
    def __init__(self, pcontent, pwner):
        self.content = pcontent
        self.owner = pwner
    
    def get_content(self):
        return self.content
        
    def get_cont(self):
        return self.get_content()
        
    def get_type(self):
        return self.content.get_type()
        
    def get_owner(self):
        return self.owner
        
    def update(self):
        if self.get_type() == "Event":
            self.content.update() # < currently dead code
