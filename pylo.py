import ee
import be

def main():
    deck_1 = ["North American Beaver", "North American Beaver", "North American Beaver",
              "Steller Sea Lion", "Steller Sea Lion", "Steller Sea Lion",
              "Giant Kelp", "Giant Kelp", "Giant Kelp",
              "Himalayan Blackberry", "Himalayan Blackberry", "Himalayan Blackberry",
              "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini"]
              
              
              
    deck_2 = ["Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini",
              "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini",
              "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini",
              "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini",
              "Hypsibius dujardini", "Hypsibius dujardini", "Hypsibius dujardini"]
    # TODO: - loader/saver for .phylo-files (i.e. decks; .deck-files?)
    # TODO: implement move/flight etc.
    on = "EVOLUTION ADMIN CHARLES DARWIN"
    hn = raw_input("\n\n\nYour name: ")
    hc_1 = 0
    hc_2 = 0
    is_story = True
    Human = ee.Entity(hn, deck_1, hc_1, 0)
    AI = ee.Entity(on, deck_2, hc_2, 1)
    test = be.Battle([Human, AI], is_story)
    test.run() # <^ rule of cool

if __name__ == "__main__":
    main()
