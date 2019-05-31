from abc import ABC
from abc import abstractmethod

from equilibrium.actors.base_actor import BaseActor
from vpython import vector


class BaseDrawer(ABC):

    def __init__(self, actor: BaseActor):
        self.actor = actor
        self.object = None

    def get_vector(self):
        pos = self.actor.position
        return vector(pos.x, pos.y, pos.z)

    def update(self):
        self.actor.update()
        self.object.pos = self.get_vector()

    @abstractmethod
    def draw(self):
        pass
