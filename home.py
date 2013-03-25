class Home(object):
    def __init__(self, pid, pwner):
        self.name = "Home card"
        self.terrain = [0, 1, 2, 3, 4, 5, 6]
        self.climate = [0, 1, 2, 3]
        self.foodchain = 9001 # not applicable
        self.scale = 0
        self.is_meat = False
        self.owner = pwner
        self.id = pid # for different home cards # TODO

    def get_name(self):
        return self.name
        
    def get_owner(self):
        return self.owner
        
    def is_meat(self):
        return self.is_meat
        
    def get_type(self):
        return "Home"
        
    def get_terrain(self):
        return self.terrain
        
    def get_climate(self):
        return self.climate

    def get_scale(self):
        return self.scale
        
    def get_foodchain(self):
        return self.foodchain
        
    def update(self): # called on entire field
        pass
