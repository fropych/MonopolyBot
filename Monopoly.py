class Monopoly:
    def  __init__(self, id):
        self.id = id
        self.tiles = []
    @property
    def active(self):
        owners = set([tile.owner for tile in self.tiles])
        if len(owners) == 1 and None not in  owners:
            return True
        return False
    
    def addTile(self, Tile):
        self.tiles.append(Tile)

