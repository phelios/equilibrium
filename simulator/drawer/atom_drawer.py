from vpython import color, sphere

from equilibrium.actors.atom import Atom
from simulator.drawer.base_drawer import BaseDrawer


class AtomDrawer(BaseDrawer):
    def draw(self):
        self.object = sphere(pos=self.get_vector(), radius=self.actor.size, color=color.red)
