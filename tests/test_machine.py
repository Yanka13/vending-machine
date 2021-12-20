
import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):

    #test that an agent can refill the machine
    def test_agent_can_refill_A(self):

        # Instanciate minimal rack and machine set up
        racks = [Rack("A", "", 100)]
        machine = Machine(racks) #Machine that accepts "A" product

        # Machine refilled with 10 biscuits "A"
        machine.refill("A", 10)

        # Assert that there is  10  biscuits "A" in the machine
        self.assertEqual(machine.racks["A"].quantity , 10)

    #User can buy an article
    def test_user_can_buy_article_A(self):

        # instanciate minimum machine set up with empty stock
        racks = [Rack("A", "", 100)]

        machine = Machine(racks, 0)

        machine.refill("A", 1)

        # user insert one dollar
        machine.insert(Coin.DOLLAR)

        #user orders product A
        outcome = machine.press("A")

        # assertions
        self.assertTrue(outcome)
        self.assertEqual(machine.racks["A"].quantity, 0)
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)
        self.assertEqual(machine.amount, 0)


    #User can get his change back
    def test_user_can_get_change_back(self):

        # instanciate machine, this time with 10 coins per category
        racks = [Rack("C", "", 85)]
        machine = Machine(racks, 10) # machine that accepts bottle of water

        # Add one bottle of water to the machine
        machine.refill("C", 1)

        # user insert one dollar
        machine.insert(Coin.DOLLAR)

        #user orders one bottle of water
        outcome = machine.press("C")

        #Assert that the machine "gives back 15 cents to the users"
        self.assertEqual(machine.coins[Coin.DIME], 9)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
