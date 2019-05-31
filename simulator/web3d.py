import logging
from vpython import *

from equilibrium.actors.atom import Atom
from equilibrium.actors.world import World
from equilibrium.units.position import Position
from simulator.drawer.atom_drawer import AtomDrawer


class Simulator:
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

    def run(self):
        # world = World("Universe One")


        atoms = []

        for x in range(500):
            agent = AtomDrawer(Atom(f"H{x}"))
            agent.draw()
            atoms.append(agent)

        scene.autoscale = False

        scene.width = 1200
        scene.height = 800

        lamp = local_light(pos=atoms[0].get_vector(), color=color.yellow)
        atoms[0].object.emissive = True
        atoms[0].object.color = color.white

        # world.add(agent1)

        # counter = 0
        while True:
            rate(60)

            # counter += 1
            for atom in atoms:
                atom.update()

            lamp.pos = atoms[0].get_vector()

