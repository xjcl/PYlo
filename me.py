# move engine
from shlex import split
from is_number import is_number
import card # again, card & deck edit module is TODO
import phylo # < RMV TODO FIXME XXX

# return True to designate a legal move
# that reduces the number of moves left
# by one

def npt(pbattle, player, pcmd):
    cmds = split(pcmd)
    if pcmd == "":
        pass
    elif len(cmds) == 1 and (cmds[0] == "exit" or cmds[0] == "e" or cmds[0] == "quit" or cmds[0] == "q"):
        raise SystemExit
    elif len(cmds) > 1 and (cmds[0] == "info" or cmds[0] == "i"):
        try:
            # phylolist = []     eventlist = [] etc. TODO
            print pcmd[2:]
            lcard = card.Card(phylo.Phylo(pcmd[2:]), None)
            lcard.pprint()
        except:
            pass # print "Error. Invalid card name." # <<< might be good num
    elif len(cmds) > 1 and (cmds[0] == "info" or cmds[0] == "i"):
        if is_number(cmds[1]):
            if player.get_hand().get_card(int(cmds[1])):
                player.get_hand().get_card(int(cmds[1])).pprint()
    elif len(cmds) == 1 and (cmds[0] == "field" or cmds[0] == "f"):
        pbattle.get_field().pprint()
    elif len(cmds) == 1 and (cmds[0] == "hand" or cmds[0] == "h"):
        player.get_hand().pprint()
    elif len(cmds) == 1 and (cmds[0] == "cards_in_hands" or cmds[0] == "cih"):
        to_p = pbattle.get_cards_in_hands()
        for i in range(pbattle.get_number_of_players()):
            print "%s: %i" % (pbattle.players[i].get_name(), to_p[i])
    elif len(cmds) == 1 and (cmds[0] == "cards_in_decks" or cmds[0] == "cid"):
        to_p = pbattle.get_cards_in_decks()
        for i in range(pbattle.get_number_of_players()):
            print "%s: %i" % (pbattle.players[i].get_name(), to_p[i])
    elif len(cmds) == 1 and (cmds[0] == "pass" or cmds[0] == "p"):
        print "%s passed." % (player.get_name())
        return True
    elif len(cmds) == 2 and (cmds[0] == "discard" or cmds[0] == "d"):
        if is_number(cmds[1]):
            if 0 <= int(cmds[1]) < player.get_hand().get_size():
                lcard = player.discard(int(cmds[1]))
                if lcard and player.get_cards_left() >= 3:
                    player.draw(3)
                    print "%s discarded %s and drew three cards." % (player.get_name(), lcard.get_content().get_name())
                    return True
    elif len(cmds) == 4 and (cmds[0] == "lay" or cmds[0] == "l"):
        if is_number(cmds[1]) and is_number(cmds[2]) and is_number(cmds[3]):
            lcard = player.get_hand().pop(int(cmds[1]))
            if lcard:
                print "DEBUG: lcard is"
                if pbattle.get_field().square_exits(int(cmds[2]), int(cmds[3])):
                    print "DEBUG: square exits"
                    if pbattle.get_field().get_square(int(cmds[2]), int(cmds[3])).lay(lcard):
                        pbattle.get_field().correct_size(int(cmds[2]), int(cmds[3]))
                        return True
                player.get_hand().insert(int(cmds[1]), lcard) # if lcard has been popped but cannot be laid
                                                              # ^ wow that sounded really wrong
    
    
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
