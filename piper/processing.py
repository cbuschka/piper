from asyncio import Queue

class Processor(object):
  def __init__(self, graph):
    self.graph = graph
    self.queue = None

  async def add_action(self, *actions):
    for action in actions:
      print("enqueuing action={}...".format(action))
      await self.queue.put(action)

  async def activate_node(self, node, input):
    print("activating node={} with value={}...".format(node, input))
    successors = [succ_node for node_id, succ_node in self.graph.nodes.items() if node.id in succ_node.dependencies]
    await node.activate(input, successors, self)

  async def process(self, input):
    self.queue = Queue()
    start_node = self.graph.nodes["start"]
    await self.activate_node(start_node, input)
    while not self.queue.empty():
      action = await self.queue.get()
      print("executing action={}...".format(action))
      await action(self)
