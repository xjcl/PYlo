class Square(object):
    def __init__(self, pfield, py, px, pcard):
        self.field = pfield
        self.x = px
        self.y = py
        if pcard:
            self.stack = [pcard] # empty (None) or list
        else:
            self.stack = None
            
    def lay_on_top(self, pcard):
        if self.stack:
            self.stack.append(pcard)
        else:
           self.stack = [pcard]
        
    def get_stack(self):
        return self.stack
                        
    def update(self):
        if self.stack:
            for lcard in self.stack[::-1]:
                lcard.update()

    def get_left(self):
        return self.field[self.y][self.x-1]

    def get_right(self):
        return self.field[self.y][self.x+1]

    def get_up(self):
        return self.field[self.y-1][self.x]

    def get_down(self):
        return self.field[self.y+1][self.x]
        
    def has_None(self):
        if self.stack:
            return True
        return False
        
    def move_right(self): # called by field when card is played on the left
        self.x += 1
                
    def move_down(self): # called by field when card is played on the left
        self.y += 1
