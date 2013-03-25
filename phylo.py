# handles phylomon
import phylo_dic
#from copy import hardcopy

class Phylo(object):
    def __init__(self, pname):
        self.dic = phylo_dic.get(pname)
        
        self.common = self.dic["common"]
        self.latin = self.dic["latin"]
        self.alt = self.dic["alt"]
        self.is_meat = self.dic["is_meat"]
        self.scale = self.dic["scale"]
        self.foodchain = self.dic["foodchain"]
        self.diet = self.dic["diet"]
        self.points = self.dic["points"]
        self.tree = self.dic["tree"]
        self.terrain = self.dic["terrain"]
        self.climate = self.dic["climate"]
        self.move = self.dic["move"]
        self.flight = self.dic["flight"]
        self.spread = self.dic["spread"]
        self.artist = self.dic["artist"]
        self.img_url = self.dic["img_url"]
        self.ofr = self.dic["ofr"]
    
        self.move_left = self.move # left as in left over, dummy.
    
    def own_foodchain_rules(self, to_eat):
        if self.ofr == 0:
            return None
    
    def update(self):
        self.moveleft = self.move
        
    def get_type(self):
        return "Phylo"
    
    def get_scale(self):
        return self.scale
        
    def is_meat(self):
        return self.is_meat
        
    def get_terrain(self):
        return self.terrain
        
    def get_climate(self):
        return self.climate
        
    def get_foodchain(self):
        return self.foodchain
        
    def get_diet(self):
        return self.diet
        
    def get_name(self):
        return self.common # include latin name?
        
    def get_dic(self):
        return self.dic
