from Field import Field
from Player import Player

A = Player(1, 1000)
B = Player(2, 2000)
field = [{"type": "Tile", "monopoly_id": 0},
        {"type": "Tile", "monopoly_id": 1},
        {"type": "Tile", "monopoly_id": 2},
        {"type": "Tile", "monopoly_id": 3},
        {"type": "Tile", "monopoly_id": 4},
        {"type": "Tile", "monopoly_id": 5},
        {"type": "Tile", "monopoly_id": 6},
        {"type": "Tile", "monopoly_id": 7},
        {"type": "Tile", "monopoly_id": 8},
        {"type": "Tile", "monopoly_id": 9},
        {"type": "Tile", "monopoly_id": 10},
        {"type": "Tile", "monopoly_id": 11},
        {"type": "Tile", "monopoly_id": 12},
        {"type": "Tile", "monopoly_id": 13},]

F = Field([[A, 0], [B, 0]], field)
F.show()