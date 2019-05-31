from abc import ABC
from abc import abstractmethod

from equilibrium.actors.base_actor import BaseActor
from vpython import vector

from equilibrium.units.position import Position


class BaseDrawer(ABC):

    def __init__(self, actor: BaseActor):
        self.actor = actor
        self.scale = 100
        self.object = None

    def get_vector(self):
        pos = self.actor.position
        return vector(pos.x/self.scale, pos.y/self.scale, pos.z/self.scale)

    def update(self):
        self.actor.update()
        self.redraw()

    def move(self, position: vector):
        self.actor.position = Position(position.x, position.y, position.z)
        self.redraw()

    def redraw(self):
        self.object.pos = self.get_vector()

    @abstractmethod
    def draw(self):
        pass
