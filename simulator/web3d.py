import logging
from vpython import *

from equilibrium.actors.atom import Atom
from equilibrium.actors.world import World
from simulator.drawer.atom_drawer import AtomDrawer


class Simulator:
    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)

    def run(self):
        # world = World("Universe One")

        atoms = []

        for x in range(5):
            agent = AtomDrawer(Atom("H"))
            agent.draw()
            atoms.append(agent)


        # world.add(agent1)

        while True:
            rate(60)

            for atom in atoms:
                atom.update()
