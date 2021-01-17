class Room:
    def __init__(self, room_name, guest_limit):
        self.room_name = room_name
        self.song_list = []
        self.guests = []
        self.guest_limit = guest_limit

    
    def add_song(self, song):
        self.song_list.append(song)

    
    def add_guest(self, guest):
        if len(self.guests) == self.guest_limit:
            return "Sorry, no space left!"
        else:
            self.guests.append(guest)
        

    def remove_guest(self, guest):
        self.guests.remove(guest)
    
    