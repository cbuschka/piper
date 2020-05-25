from .graph import Node

class MapNode(Node):
  def __init__(self, id, dependencies=None, mapper=None):
    super().__init__(id, dependencies)
    self.mapper = mapper

  async def activate(self, input, successors, processor):
    await processor.add_action(*[MapAction(input, node, self.mapper) for node in successors])

class MapAction(object):
  def __init__(self, value, node, mapper):
    self.value = value
    self.node = node
    self.mapper = mapper or (lambda x: x)

  async def __call__(self, processor):
      await processor.activate_node(self.node, self.mapper(self.value))

  def __repr__(self):
    return "<MapAction node={} value={}>".format(self.node, self.value)



