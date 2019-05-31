from random import randint

from equilibrium.actors.base_actor import BaseActor


class Atom(BaseActor):

    def __init__(self, name):
        super().__init__(name)
        self.size = 10

    def update(self):
        self.position.x += randint(-1, 1)
        self.position.y += randint(-1, 1)
        self.position.z += randint(-1, 1)

        super().update()
