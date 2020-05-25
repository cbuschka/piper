from uuid import uuid4 as genuuid
from .activate_action import ActivateAction

class Node(object):
  def __init__(self, id=None, dependencies=None):
    self.id = id or genuuid()
    self.dependencies = dependencies or []

  async def activate(self, input, successors, processor):
    await processor.add_action(*[ActivateAction(input, successor) for successor in successors])

  def __repr__(self):
    return "<{} id={}>".format(type(self).__name__,self.id)


class Graph(object):
  def __init__(self):
    self.nodes = {}

  def add_node(self, node):
    self.nodes[node.id] = node
