class Horse:
    x_distance = 0
    _sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self):
         self.sound = super()._sound
         self.sound = super().sound

    def move(self, dx, dy):
            super().run(dx)
            super().fly(dy)
    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus
    def voice(self):
        return (self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos()), p1.move(-5, 20)
print(p1.get_pos())

p1.voice()



