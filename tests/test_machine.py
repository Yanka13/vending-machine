
import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):

    #test that an agent can refill the machine
    def test_agent_can_refill_A(self):

        # Instanciate minimal rack and machine.
        racks = [Rack("A", "", 100)]
        machine = Machine(racks)

        # I need to refill this machine with 10 biscuits "A"
        machine.refill("A", 10)

        # Assert that I have 10  biscuits "A" in my machine
        self.assertEqual(machine.racks["A"].quantity , 10)

    #User can buy an article
    def test_user_can_buy_article_A(self):

        # instanciate minimum machine
        racks = [Rack("A", "", 100)]

        machine = Machine(racks, 0)

        machine.refill("A", 1)

        # user insert money
        machine.insert(Coin.DOLLAR)

        #user choose product A
        outcome = machine.press("A")

        # assertions
        self.assertTrue(outcome)
        self.assertEqual(machine.racks["A"].quantity, 0)
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)

    #User can get his change back
    def test_user_can_get_change_back(self):

        # instanciate machine (this time with 10 coins each)
        racks = [Rack("C", "", 85)]
        machine = Machine(racks, 10)
        machine.refill("C", 1)

        # user insert money
        machine.insert(Coin.DOLLAR)

        #user choose product A
        outcome = machine.press("C")

        #Assert that there are 15 cents left
        self.assertEqual(machine.coins[Coin.DIME], 9)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
