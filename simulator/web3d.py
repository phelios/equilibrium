import logging
from vpython import scene, local_light, color, rate
import random

from equilibrium.actors.atom import Atom
from equilibrium.units import direction
from equilibrium.units.position import Position
from simulator.drawer.atom_drawer import AtomDrawer
from simulator.drawer.atom_drawer_box import AtomDrawerBox


class Simulator:
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

    @staticmethod
    def _rand_direction():
        directions = [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST]
        return directions[random.randint(0, len(directions) - 1)]

    @staticmethod
    def rand_coordinate():
        def rand():
            return random.randint(-1000, 1000)
        return Position(rand(), rand(), rand())

    def run(self):
        atoms = []

        for x in range(500):

            atom = Atom(f"H{x}")
            atom.size = random.randint(1, 100)
            atom.direction = self._rand_direction()
            atom.speed = random.randint(1, 10)
            atom.position = self.rand_coordinate()

            agent = AtomDrawerBox(atom)
            agent.draw()
            atoms.append(agent)

        scene.autoscale = False

        scene.width = 1200
        scene.height = 800

        lamp = local_light(pos=atoms[0].get_vector(), color=color.yellow)
        atoms[0].object.emissive = True
        atoms[0].object.color = color.white

        while True:
            rate(60)

            for atom in atoms:
                atom.update()

            lamp.pos = atoms[0].get_vector()

