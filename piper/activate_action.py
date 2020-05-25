class ActivateAction(object):
  def __init__(self, value, nodes):
    self.value = value
    self.nodes = nodes if isinstance(nodes, list) else [nodes]

  async def __call__(self, processor):
    for node in self.nodes:
      await processor.activate_node(node, self.value)

  def __repr__(self):
    return "<ActivateAction nodes={} value={}>".format(self.nodes, self.value)
