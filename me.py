# move engine
from shlex import split

def npt(player, pcmd):
    cmds = split(pcmd)
    if len(cmds) == 1 and cmds[0] == "pass":
        print "%s passed." % (player.get_name())
    
    
    
    
    """if True:
        cmds = split(pcmd)
        if cmds[0] == "grow":
            lPhylos = player.get_active_phylos()
            lPhylo = lPhylos[int(cmds[1])] # FIXME isnumber()
            if random.randint(1, lPhylo.get_scale()) == 1:
                lPhylo.set_scale(lPhylo.get_scale()+1)
                print
                print "The %s of %s grew by one. [scale=%d]" % \
                (lPhylo.get_name(), player.get_name(), lPhylo.get_scale())
            else:
                print
                print "The growing attempt of %s on %s failed." % \
                (player.get_name(), lPhylo.get_name())"""
