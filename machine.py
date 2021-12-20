from enum import Enum

class Rack():
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTIER = 25
    DOLLAR = 100


class Machine():
    def __init__(self, racks, coins_count=10):
        self.racks = dict((rack.code, rack) for rack in racks) # A dict with key="A", value= Rack("A"...)
        self.coins = dict((coin, coins_count) for coin in Coin) # A dict with key=Coin.DOLLAR object, value=10
        self.amount = 0

    #refill stock
    def refill(self, code, quantity ):
        self.racks[code].quantity += quantity

    #insert monney
    def insert(self, coin ):
        self.coins[coin] += 1
        self.amount += coin.value

    #utils
    def __give_change_back(self, change):
        if change == 0:
            return True
        else:
            for coin in reversed(Coin):
                count = change // coin.value
                change =  change % coin.value
                self.coins[coin] -= 1
            return True

    # press
    def press(self, code):
        #check if user has the right to buy, enough money
        rack = self.racks[code]
        if self.amount >= rack.price:

            if rack.quantity > 0:
                rack.quantity -= 1
                change = self.amount - rack.price
                self.__give_change_back(change)
                self.amount -= rack.price
                return True
            else:
                # TO DO : give feedback to user that stock are empty
                return False
        else:
            #TO DO : give feedback to user explaining he has not enough money
            return False


if __name__ == "__main__":

    racks = [Rack("A","", 100)]
    racks = dict((rack.code, rack) for rack in racks)
    print(racks)

    for coin in Coin:
        print(coin, coin.value)


