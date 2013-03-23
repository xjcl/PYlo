d = {
    "North American Beaver": {
        "common": "North American Beaver",
        "latin": "Castor canadensis",
        "alt": "Castor canadensis is a national symbol for Canada.",
        
        "scale": 6,
        "foodchain": 2,
        "diet": 2,
        "points": 5,
        "tree": ["Animalia", "Chordata", "Mammalia"], # evolutionary tree info
        
        "terrain": [0, 1, 5],
        "climate": [1, 2],
        
        "move": 2,
        "flight": 0,
        "spread": 0,
        
        "artist": "Image by Adam Smith",
        "img_url": "http://rupted.deviantart.com/"},
        
        
        
    "Hypsibius dujardini": { # TARDIGRADES OMG :D SO COOL.
        "common": "Hypsibius dujardini",
        "latin": "Hypsibius dujardini",
        "alt": "Hypsibius dujardini is the only animal known to be able to survive the vacuum of space.",
        
        "scale": 3,
        "foodchain": 2,
        "diet": 2,
        "points": 3,
        "tree": ["Animalia", "Tardigrada", "Eutardigrada"],
        
        "terrain": [5, 6],
        "climate": [0, 1, 2, 3],
        
        "move": 0.5,
        "flight": 0,
        "spread": 0,
        
        "artist": "Image by Akela Taka",
        "img_url": "akelataka.deviantart.com/"}
    }
    
    
    
    
    
    
terrain = ["forest", "grasslands", "tundra", "urban", "desert", "fresh water", "salt water"]
climate = ["cold", "cool", "warm", "hot"]
diet = ["photosynthetic", "molecular", "herbivore", "omnivore", "carnivore"] # 1 might also be "special"

def get(pname):
    if pname in d:
        return d[pname]