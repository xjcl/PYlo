class Square(object):
    def __init__(self, pfield, py, px, pcard):
        self.field = pfield
        self.x = px
        self.y = py
        if pcard:
            self.stack = [pcard] # empty (None) or list
        else:
            self.stack = None
    
    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):
        self.y = new_y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def just_played_invasive(self):
        dead_sc = self.pop_phylo_card()
        print "%s (%s) on square %d %d was removed (INVASION)."\
        % (dead_sc.get_cont().get_name(), dead_sc.get_owner.get_name(), self.y, self.x)
        for neigh_sq in self.get_neigh():
            pc = None
            pc = neigh_sq.get_phylo_card()
            if pc:  
                if not neigh_sq.check_phylo_card(pc):
                    discarded_pc = neigh_sq.pop_phylo_card()
                    print "%s (%s) on square %d %d was removed due to a lack of compatibility with the INVASIVE species %s."\
                    % (discarded_pc.get_cont().get_name(), discarded_pc.get_owner().get_name(),\
                    neigh_sq.get_y(), neigh_sq.get_x, self.get_phylo_card().get_cont().get_name())
    
    def is_compatible(self, p1, p2):
        terrain_match = False
        for a_terrain in p1.get_terrain():
            if a_terrain in p2.get_terrain():
                terrain_match = True
                break
        for a_climate in p1.get_climate():
            if a_climate in p2.get_climate():
                return terrain_match # if this code is executed, climate_match == True
                
    def good_foodchain(self, new_p, old_p):
        if new_p.get_foodchain() == 1:
            return True
        else:
            if new_p.get_diet() == 3: # omnivore
                if new_p.get_foodchain() > old_p.get_foodchain():
                    if old_p.is_meat() and new_p.get_scale() > old_p.get_scale():
                        return True
                    elif not old_p.is_meat():
                        return True
            elif new_p.get_foodchain() == old_p.get_foodchain() + 1:
                if new_p.get_diet() == 4 and old_p.is_meat() and new_p.is_meat(): # carnivore
                    if new_p.get_scale() > old_p.get_scale():
                        return True
                else:
                    return True        
        return False    
    
    def test_foodchain(self, new_p, old_p):
        if not new_p.own_foodchain_rules(old_p):
            return self.good_foodchain(new_p, old_p)    
    
    def check_phylo_card(self, pcard):
        lPhylo = pcard.get_content()
        compt, foodc = False, False
        for neigh_sq in self.get_neigh():
            neigh_sq = self.get_down()
            print "DEBUG: neigh_sq"
            neigh_p = None
            try:
                neigh_c = neigh_sq.get_phylo_card()
                neigh_p = neigh_c.get_content()
                print "DEBUG: neigh_sq has phylo (or home)"
            except:
                print "DEBUG: neigh_sq has None"
            if neigh_p:
                if self.is_compatible(lPhylo, neigh_p):
                    compt = True
                if self.test_foodchain(lPhylo, neigh_p):
                    foodc = True
        print "DEBUG: compt: %r; foodc: %r" % (compt, foodc)
        return compt and foodc
            
    def lay(self, pcard):
        if not self.has_None():
            print "DEBUG: sq has some"
            if pcard.get_type() == "Phylo" and pcard.is_invasive != False:
                print "DEBUG: invasion attempt"
                if pcard.get_cont().check_invasion(self.get_phylo_card().get_cont()):
                    print "%s played INVASIVE species %s on square %d %d."\
                    % (pcard.get_owner().get_name(), pcard.get_cont().get_name(), self.y, self.x)
                    self.just_played_invasive()
                    return True
            elif pcard.get_type() == "Event":
                if self.check_event(pcard): # so that it is not this one function that does everything
                    self.stack.append(pcard) # TODO FIXME
                    self.stack[-1].get_content().play(self)
                    return True
        else:
            if pcard.get_type() == "Phylo":
                print "DEBUG: Normal phylo lay"
                if self.check_phylo_card(pcard): # so that it is not this one function that does everything
                    self.stack = [pcard]
                    print "%s played species %s on square %d %d."\
                    % (pcard.get_owner().get_name(), pcard.get_cont().get_name(), self.y, self.x)
                    if pcard.get_cont().is_pollinator():
                        self.field.set_pollinator(True)
                    return True
        
    def get_stack(self):
        return self.stack
                        
    def update(self):
        if self.stack:
            for lcard in self.stack[::-1]:
                lcard.update()

    def get_left(self):
        try:
            return self.field.get_data()[self.y][self.x-1]
        except:
            return None

    def get_right(self):
        try:
            return self.field.get_data()[self.y][self.x+1]
        except:
            return None

    def get_up(self):
        try:
            return self.field.get_data()[self.y-1][self.x]
        except:
            return None

    def get_down(self):
        try:
            return self.field.get_data()[self.y+1][self.x]
        except:
            return None
    
    def get_neigh(self): # get neighbours
        return [self.get_up(), self.get_right(), self.get_down(), self.get_left()]
        
    def has_None(self): # does the exact opposite of its name...
        if self.stack:
            return False
        return True
        
    def get_phylo_card(self):
        if not self.has_None():
            print "DEBUG: stack has some"
            l_maybe_Phylo_card = self.stack[0]
            if 1:#l_maybe_Phylo.get_type() != "Home card": # and not l_maybe_Phylo.is_invasive(): # invasives on bottom have done their job
                if not l_maybe_Phylo_card.get_cont().is_parasitic():
                    print "DEBUG: return Phylo"
                    return self.stack[0]
                else:
                    print "DEBUG: return Phylo on top of parasite"
                    return self.stack[1] # BOTH INVASIVE AND PARASITIC? MULTIPLE PARASITIC? INVASIVE ON INVASIVE? TODO FIXME
        
    def pop_phylo_card(self):
        if not self.has_None():
            l_maybe_Phylo = self.stack[0]
            if l_maybe_Phylo.get_type() != "Home card": # and not l_maybe_Phylo.is_invasive(): # invasives on bottom have done their job
                self.field.check_pollinator()
                if not l_maybe_Phylo.is_parasitic():
                    return self.stack.pop(0)
                else:
                    return self.stack.pop(1)
            
    def move_right(self): # called by field when card is played on the left
        self.x += 1
                
    def move_down(self): # called by field when card is played above
        self.y += 1
