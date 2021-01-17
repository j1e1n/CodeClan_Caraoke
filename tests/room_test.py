import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1")
        self.song = Song("Africa", "Toto")
        self.guest = Guest("Elton John")

    
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.room_name)

    
    def test_room_start_with_empty_song_list(self):
        self.assertEqual(0, len(self.room.song_list))

    
    def test_room_starts_with_empty_guest_list(self):
        self.assertEqual(0, len(self.room.guests))


    def test_can_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.song_list))

    
    def test_can_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))