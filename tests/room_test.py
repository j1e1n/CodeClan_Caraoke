import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1")

    
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.room_name)

    
    def test_room_start_with_empty_song_list(self):
        self.assertEqual(0, len(self.room.song_list))

    
    def test_room_starts_with_empty_guest_list(self):
        self.assertEqual(0, len(self.room.guests))