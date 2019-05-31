import random

from vpython import sphere, vector

from simulator.drawer.base_drawer import BaseDrawer


class AtomDrawer(BaseDrawer):
    def draw(self):
        color = vector(self.random_float(), self.random_float(), self.random_float())
        self.object = sphere(pos=self.get_vector(), radius=self.actor.size/self.scale, color=color)

    def random_float(self):
        return random.uniform(0, 1)
