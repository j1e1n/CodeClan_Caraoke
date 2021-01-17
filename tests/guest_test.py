import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Elton", 30.00, "Purple Rain")
        self.room = Room("Room 1", 3, 5.00, 100.00)
        

    
    def test_guest_has_name(self):
        self.assertEqual("Elton", self.guest_1.name)


    def test_guest_can_pay_entry_fee(self):
        self.guest_1.pay_entry_fee(self.room.entry_fee)
        self.assertEqual(25.00, self.guest_1.wallet)


   