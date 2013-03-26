# handles phylomon
import phylo_dic
#from copy import hardcopy

class Phylo(object):
    def __init__(self, pname):
        self.dic = phylo_dic.get(pname)
        
        self.common = self.dic["common"]
        self.latin = self.dic["latin"]
        self.alt = self.dic["alt"]
        self.tree = self.dic["tree"]
        
        self.meat = self.dic["is_meat"]
        self.plankton = self.dic["is_plankton"]
        self.algae = self.dic["is_algae"]
        self.invasive = self.dic["is_invasive"]
        self.parasitic = self.dic["is_parasitic"]
        self.pollinator = self.dic["is_pollinator"]
        
        self.scale = self.dic["scale"]
        self.foodchain = self.dic["foodchain"]
        self.ofr = self.dic["ofr"]
        self.diet = self.dic["diet"]
        self.points = self.dic["points"]
        
        self.terrain = self.dic["terrain"]
        self.climate = self.dic["climate"]
        
        self.move = self.dic["move"]
        self.flight = self.dic["flight"]
        self.spread = self.dic["spread"]
        
        self.artist = self.dic["artist"]
        self.img_url = self.dic["img_url"]
    
        self.move_left = self.move # left as in left over, dummy.
    
    def get_type(self):
        return "Phylo"
    
    def get_scale(self):
        return self.scale
        
    def get_tol(self):
        return self.tree
        
    def get_tree(self):
        return self.tree
        
    def is_meat(self):
        return self.meat
        
    def is_pollinator(self):
        return self.pollinator
        
    def is_invasive(self):
        return self.invasive
        
    def is_parasitic(self):
        return self.parasitic
        
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
        
    def own_foodchain_rules(self, to_eat):
        if self.ofr == 0:
            return None
    
    def update(self):
        self.moveleft = self.move
        
    def is_invasive(self):
        if self.invasive == False:
            return False
        return True # deals with numbers
        
    def check_invasion(self, p_invaded):
        if self.invasive == 1 and p_invaded.get_scale() == self.scale and p_invaded.get_tol()[0] == self.tree[0]:
            return True
        return False
        
        # invasive rules:
        # 1: same kingdom, same scale
        
