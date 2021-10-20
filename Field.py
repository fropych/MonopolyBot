from Monopoly import Monopoly
from Tile import Tile

class Field:
    def __init__(self, Players, field):
        self.Players = Players
        self.Tiles = []
        self.Monopolys = []
        self.filed = field
        self.create_monopolys()
        self.create_field()

    def create_monopolys(self):
        for tile in self.field[::-1]:
            if tile["monopoly_id"] != None:
                self.Monopolys = [Monopoly() for _ in range(tile["monopoly_id"] + 1)]

    def create_field(self):
        id = 0
        for tile in self.field:
            if tile["type"] == "Tile":
                self.Tiles.append(Tile(id, 100, 50, self.Monopolys[tile["monopoly_id"]]))
            id += 1
