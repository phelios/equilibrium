import logging

from equilibrium.units import direction
from equilibrium.units.position import Position


class BaseActor:
    def __init__(self, name):
        self.name = name
        self.position = Position(0, 0, 50)
        self.size = 100
        self.speed = 0
        self.direction = direction.NORTH
        self.composition = []

    def place(self, x, y, z):
        self.position.x = x
        self.position.y = y
        self.position.z = z

    def add(self, actor):
        self.composition.append(actor)

    def update(self):
        for actor in self.composition:
            actor.update()

        logging.debug(self)

    def __repr__(self):
        summary = {
            'name': self.name,
            'position': self.position
        }
        return f"{summary}"
