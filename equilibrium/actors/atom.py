from random import randint

from equilibrium.actors.base_actor import BaseActor


class Atom(BaseActor):

    def __init__(self, name):
        super().__init__(name)
        self.size = 10

    def update(self):
        self.position.x += self.random_movement()
        self.position.y += self.random_movement()
        self.position.z += self.random_movement()

        super().update()

    def random_movement(self):
        return randint(-self.speed, self.speed)
