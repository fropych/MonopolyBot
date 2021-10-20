class Player:
    def __init__(self, id, money):
        self.id = id
        self.money = money
        self.tilesOwn = []
        self.dead = False

    def set_money(self, amount):
        self.money += amount
        if self.money < 0:
            if self.capital < -self.money:
                self.dead = True
                return
            return self.hostage()

    def hostage(self):
        tilesID = [tile.id for tile in self.tilesOwn]
        print("Выбирите поле для залога: ",  end="")
        print(", ".join(tilesID))
        
    def user_input(self):
        #сделать проверку пользователя
        usr_input = input()
        return int(usr_input) if usr_input.isdigit() else usr_input

    @property
    def capital(self):
        ans = 0
        for tile in self.tilesOwn:
            ans += tile.cost
        return ans
    
        

