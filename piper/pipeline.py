from .graph import Graph, Node
from .processing import Processor
from .flat_map_node import FlatMapNode
 

class Pipeline(object):
  def __init__(self, graph):
    self.graph = graph

  async def process(self, input):
    processor = Processor(self.graph)
    return await processor.process(input)
 

class PipelineBuilder(object):
  def __init__(self):
    self.graph = Graph()
    self.graph.add_node(Node("start"))
    self.prev_node = "start"

  def flatmap(self):
    new_node_id = "flatmap"
    self.graph.add_node(FlatMapNode(new_node_id, [self.prev_node]))
    self.prev_node = new_node_id
    return self

  def end(self):
    self.graph.add_node(Node("end", [self.prev_node]))
    return Pipeline(self.graph)

def pipeline():
  return PipelineBuilder()

  
  
