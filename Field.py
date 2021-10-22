from Monopoly import Monopoly
from Tile import Tile
from Dice import Dice
from random import randint

class Field:
    def __init__(self, Players, field):
        self.turn = 0
        self.Players = Players # [Player, position]
        self.Tiles = []
        self.Monopolys = []
        self.field = field
        self.create_monopolys()
        self.create_field()

    def create_monopolys(self):
        for tile in self.field[::-1]:
            if tile["monopoly_id"] != None:
                self.Monopolys = [Monopoly(id) for id in range(tile["monopoly_id"] + 1)]
                break

    def create_field(self):
        id = 0
        for tile in self.field:
            if tile["type"] == "Tile":
                self.Tiles.append(Tile(id, 100, 50, self.Monopolys[tile["monopoly_id"]]))
            id += 1

    def next_turn(self):
        pass

    def show(self):
        sizeField = len(self.field)
        field = ["z"] * sizeField 
        for player in self.Players:
            position = player[1]
            if field[position] == "z":
                field[position] = [player[0].id,]
                continue
            field[position].append(player[0].id)
        line_size = int( (sizeField + 4)/4 )
        first_line = field[0:line_size]
        second_line = field[line_size:(2*line_size - 2)]
        third_line = field[(2*line_size - 2):(3*line_size - 2)] 
        fourth_line = field[(3*line_size - 2):(4*line_size - 4)]
        for i in first_line:
            print("%10s" % i, end="")
        print('')
        for i in range(len(fourth_line)):
            print('')
            print("%10s" % fourth_line[i], end="")
            print(f"%{(line_size-1)*10}s" % second_line[i])
        print('')
        for i in third_line:
            print("%10s" % i, end="")
        print('')


        


