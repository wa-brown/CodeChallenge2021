class Antenna():
    def __init__(self, id, range, connection_speed):
        self.id = id
        self.range = range
        self.connection_speed = connection_speed

    def set_coords(self, w, h):
        self.width = w
        self.height = h