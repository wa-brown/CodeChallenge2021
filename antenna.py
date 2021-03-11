class Antenna():
    def __init__(self, id, range, connection_speed):
        self.id = id
        self.range = range
        self.connection_speed = connection_speed

    def set_coords(self, x, y):
        self.x = x
        self.y = y