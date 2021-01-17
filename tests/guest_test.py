import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Elton", 30.00)
        self.room = Room("Room 1", 3, 5.00, 100.00)
        

    
    def test_guest_has_name(self):
        self.assertEqual("Elton", self.guest.name)


    def test_guest_can_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room.entry_fee)
        self.assertEqual(25.00, self.guest.wallet)