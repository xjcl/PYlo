# Phylo Double Dynasty!!

# Concept: Have two compatible species on each side.

import ee
import be
#import phylo # remove later

def main():
    deck_1 = ["North American Beaver", "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini"]
    h_n = raw_input("\n\n\nYour name: ")
    Human = ee.Entity(h_n, deck_1)
    AI = ee.Entity("ECOLOGY ADMIN DARWIN", deck_1)
    test = be.Battle(Human, AI)
    test.run()

if __name__ == "__main__":
    main()
