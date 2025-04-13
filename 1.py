class BigBell:
    def __init__(self):
        self.next_sound = "ding"

    def sound(self):
        print(self.next_sound)
        self.next_sound = "dong" if self.next_sound == "ding" else "ding"


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
