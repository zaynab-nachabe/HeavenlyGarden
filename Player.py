from  pynput.keyboard import Key, Listener

class Player:
    def __init__(self,pos_x,pos_y,nb_keys):
        self.nb_keys = nb_keys
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, direction):
        if direction == "z":
            self.pos_y += 1
        elif direction == "s":
            self.pos_y -= 1
        elif direction == "q":
            self.pos_x -= 1
        elif direction == "d":
            self.pos_x += 1

    def add_keys(self, keys):
        self.nb_keys += keys
        print(f"Player has now {self.nb_keys} keys !")

player = Player(0, 0, 0)
player.add_keys(3)

def on_press(key):
    try:
        key_char = key.char.lower()
        if key_char in ['z', 's', 'q', 'd']:
            player.move(key_char)
            print(f"Player moved to ({player.pos_x}, {player.pos_y})")
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

