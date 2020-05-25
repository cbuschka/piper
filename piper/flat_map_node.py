from .graph import Node

class FlatMapNode(Node):
  def __init__(self, id, dependencies=None):
    super().__init__(id, dependencies)

  async def activate(self, input, successors, processor):
    await processor.add_action(*[FlatMapAction(input, node) for node in successors])

class FlatMapAction(object):
  def __init__(self, value, node):
    self.value = value
    self.node = node

  async def __call__(self, processor):
    for item in self.value:
      await processor.activate_node(self.node, item)

  def __repr__(self):
    return "<FlatMapAction node={} value={}>".format(self.node, self.value)



