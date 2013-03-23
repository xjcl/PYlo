# Phylo Double Dynasty!!

# Concept: Have two compatible species on each side.

import ee
import be
#import phylo # remove later

def main():
    deck_1 = ["North American Beaver", "North American Beaver", "North American Beaver", "Hypsibius dujardini"]
    deck_2 = ["North American Beaver", "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini"]
    on = "EVOLUTION ADMIN CHARLES DARWIN"
    hn = raw_input("\n\n\nYour name: ")
    hc_1 = 0
    hc_2 = 0
    Human = ee.Entity(hn, deck_1, hc_1, 0)
    AI = ee.Entity(on, deck_2, hc_2, 1)
    test = be.Battle([Human, AI], True)
    test.run() # <^ rule of cool

if __name__ == "__main__":
    main()
