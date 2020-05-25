import asyncio
from piper.graph import Graph, Node
from piper.processing import Processor
from piper.flat_map_node import FlatMapNode
from piper.pipeline import pipeline

async def main():
  p = pipeline() \
    .flatmap() \
    .map(lambda x: ">{}<".format(x)) \
    .end()
  await p.process([1,2,3,4,5])

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())

