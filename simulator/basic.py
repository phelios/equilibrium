import logging
from time import sleep

from equilibrium.actors.atom import Atom
from equilibrium.actors.world import World


class Simulator:
    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)

    def run(self):
        world = World("Universe One")
        agent1 = Atom("H")

        world.add(agent1)

        while True:
            world.update()
            sleep(2)
