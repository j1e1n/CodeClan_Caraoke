class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.song_list = []
        self.guests = []

    
    def add_song(self, song):
        self.song_list.append(song)

    
    def add_guest(self, guest):
        self.guests.append(guest)
        


    
    