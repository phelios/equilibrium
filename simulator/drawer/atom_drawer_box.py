import random

from vpython import box, vector

from simulator.drawer.base_drawer import BaseDrawer


class AtomDrawerBox(BaseDrawer):
    def draw(self):
        color = vector(self.random_float(), self.random_float(), self.random_float())
        self.object = box(pos=self.get_vector(), color=color, **self.dimension())

    def random_float(self):
        return random.uniform(0, 1)

    def dimension(self):
        size = self.actor.size / self.scale

        return {
            'length': size,
            'width': size,
            'height': size
        }
