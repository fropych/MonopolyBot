class Tile:
    def __init__(self, id, cost, fee, Monopoly):
        self.id = id
        self.cost = cost
        self.sell = int(cost * 0.8)
        self.fee = fee
        self.level = 1
        self.Monopoly = Monopoly
        self.Monopoly.addTile(self)
        self.owner = None
        self.hostageON = False

    def playerOnTile(self, Player):
        if self.hostageON:
            return
        elif self.owner == None:
            return self.buyTile(self, Player)
        elif self.owner != Player.id:
            Player.set_money(-self.payment)
            self.owner.set_money(self.payment)
            
    def buyTile(self, Player):
        if Player.money < self.cost:
            print("Недостаточно средств")
            print("Аукцион")
            return "auction"

        print("Купить клетку (y/n)")
        if Player.user_input() == "y":
            Player.set_money(-self.cost)
            self.owner = Player
            print(f"Клетку {self.id}, купил игрок {Player.id}")
        elif Player.user_input() == "n":
            print("Аукцион")
            return "auction"
        else:
            print("Неверный ввод")
            self.buyTile(self, Player)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.cost}, {self.sell}, {self.fee}, {self.Monopoly.id}, {self.owner})"
    @property
    def payment(self):
        return self.fee * self.level * (2 if self.Monopoly.active else 1)
        


