class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        prop = {
            'x': self.x,
            'y': self.y,
            'z': self.z
        }

        return f"{prop}"
