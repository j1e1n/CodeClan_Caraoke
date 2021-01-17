import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 3, 5.00, 100.00)
        self.song_1 = Song("Africa", "Toto")
        self.song_2 = Song("Purple Rain", "Prince")
        self.song_3 = Song("Dancing Queen", "Abba")
        
        self.guest_1 = Guest("Elton", 30.00, "Purple Rain")
        self.guest_2 = Guest("Dolly", 40.00, "Wannabe")
        self.guest_3 = Guest("Kylie", 50.00, "Africa")
        self.guest_4 = Guest("Bruce", 50.00, "Enter Sandman")

    
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.room_name)

    
    def test_room_start_with_empty_song_list(self):
        self.assertEqual(0, len(self.room.song_list))

    
    def test_room_starts_with_empty_guest_list(self):
        self.assertEqual(0, len(self.room.guests))


    def test_can_add_song(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.assertEqual(2, len(self.room.song_list))

    
    def test_can_add_guest(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guests))


    def test_can_remove_guest(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.remove_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guests))


    def test_room_has_guest_limit(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_3)
        self.assertEqual("Sorry, no space left!", self.room.add_guest(self.guest_4))

    def test_room_can_take_entry_fee(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.take_entry_fee(self.room.entry_fee)
        self.assertEqual(110.00, self.room.total_cash)
        self.assertEqual(25.00, self.guest_1.wallet)
        self.assertEqual(35.00, self.guest_2.wallet)
        

    def test_guest_can_search_for_favourite_song_found(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_song(self.song_3)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.assertEqual("Whoo!", self.room.search_for_favourite_song(self.guest_1))


    def test_guest_can_search_for_favourite_song_not_found(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_song(self.song_3)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.assertEqual("I don't like this room.", self.room.search_for_favourite_song(self.guest_2))



    

    