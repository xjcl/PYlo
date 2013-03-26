# field engine
from se import Square

class Field(object):
    def __init__(self, phomes):
        self.homes = phomes
        self.has_pollinator = False
        if len(self.homes) == 2: # len(self.homes) == number of players
            self.data = \
            [[Square(self, 0, 0, None), Square(self, 0, 1, None),
            Square(self, 0, 2, None), Square(self, 0, 3, None)], 
            \
            [Square(self, 1, 0, None), Square(self, 1, 1, phomes[0]),
            Square(self, 1, 2, phomes[1]), Square(self, 1, 3, None)],
            \
            [Square(self, 2, 0, None), Square(self, 2, 1, None),
            Square(self, 2, 2, None), Square(self, 2, 3, None)]]
        if len(self.homes) == 4: # len(self.homes) == number of players
            self.data = \
            [[Square(self, 0, 0, None), Square(self, 0, 1, None),
            Square(self, 0, 2, None), Square(self, 0, 3, None)], 
            \
            [Square(self, 1, 0, None), Square(self, 1, 1, phomes[0]),
            Square(self, 1, 2, phomes[1]), Square(self, 1, 3, None)],
            \
            [Square(self, 2, 0, None), Square(self, 2, 1, phomes[2]),
            Square(self, 2, 2, phomes[3]), Square(self, 2, 3, None)],
            \
            [Square(self, 3, 0, None), Square(self, 3, 1, None),
            Square(self, 3, 2, None), Square(self, 3, 3, None)]]
    
    def has_pollinator():
        return self.has_pollinator
        
    def set_pollinator(pbool):
        self.has_pollinator = pbool
        
    def check_pollinator():
        self.has_pollinator = False
        for row in self.data:
            for sq in row:
                if sq.get_stack.get_phylo().is_pollinator:
                    self.has_pollinator = True
        
    def extend_right(self):
        for i in range(len(self.data)):
            self.data[i].append(Square(self, i, len(self.data[i]), None))
    
    def extend_down(self):
        self.data.append([])
        for i in range(len(self.data[-2])):
            self.data[-1].append(Square(self, len(self.data)-1, i, None))
            
    def extend_left(self):
        for rw in self.data:
            for sq in rw:
                sq.set_x(sq.get_x()+1)
        for i in range(len(self.data)):
            self.data[i].insert(0, Square(self, i, 0, None))
    
    def extend_up(self):
        for rw in self.data:
            for sq in rw:
                sq.set_y(sq.get_y()+1)
        self.data.insert(0, [])
        for i in range(len(self.data[1])):
            self.data[0].append(Square(self, 0, i, None))
            
    def correct_size(self, py, px):
        if py == 0:
            self.extend_up()
        if px == 0:
            self.extend_left()
        if py == len(self.data)-1:
            self.extend_down()
        if px == len(self.data[0])-1:
            self.extend_right()
            
    def check_all_phylo(self):
        for row in self.data:
            for sq in row:
                lPhylo_card = sq.get_stack().get_phylo_card() # I have no idea what I did there in se.py
                if not sq.check_phylo(lPhylo_card):
                    sq.pop_phylo_card()
       
    def square_exits(self, py, px):
        return 0 <= py < len(self.data) and 0 <= px < len(self.data[0]) # isnumber() in me.py
    
    def pprint(self):
        dat = []
        for y in range(len(self.data)):
            print
            print "------"*len(self.data[0])+"-"
            print "|",
            if y < 10:
                sy = " "+str(y)
            else:
                sy = str(y)
            for x in range(len(self.data[0])):
                if x < 10:
                    sx = str(x)+" "
                else:
                    sx = str(x)
                to_p = sy+","+sx
                print "\b"+to_p+"|",
                try:
                    dat.append([to_p, self.get_square(y, x).get_stack()[0].get_cont().get_name()]) # TODO # display other cards on stack
                except:
                    dat.append([to_p, "None"])
        print
        print "------"*len(self.data[0])+"-"
        print
        for tup in dat:
            print "%s: %s" % (tup[0], tup[1])
                
    def get_square(self, py, px):
        if self.square_exits(py, px):
            return self.data[py][px]
    
    def get_data(self):
        return self.data
    

    
    #def handle_move(self, pstr):
        
