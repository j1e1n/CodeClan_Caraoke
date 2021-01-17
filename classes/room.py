class Room:
    def __init__(self, room_name, guest_limit, entry_fee, total_cash):
        self.room_name = room_name
        self.song_list = []
        self.guests = []
        self.guest_limit = guest_limit
        self.entry_fee = entry_fee
        self.total_cash = total_cash

    
    def add_song(self, song):
        self.song_list.append(song)

    
    def add_guest(self, guest):
        if len(self.guests) == self.guest_limit:
            return "Sorry, no space left!"
        else:
            self.guests.append(guest)
        

    def remove_guest(self, guest):
        self.guests.remove(guest)
    
    
    def take_entry_fee(self, amount):
        for guest in self.guests:
            guest.pay_entry_fee(amount)
            self.total_cash += amount


    def search_for_favourite_song(self, guest):
        for song in self.song_list:
            if song.title == guest.favourite_song:
                return "Whoo!"
             
        return "I don't like this room."
        