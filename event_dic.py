d = {
    "Oil Spill": {
        "indexes": [[0, 0]],
        "rl": 0},
    "Species Protection": {
        "indexes": [[2, 0]],
        "rl": 0}
    }
    
def get(pname):
    if pname in d:
        return d[pname]
