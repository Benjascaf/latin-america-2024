from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

my_processor = SimpleProcessor(CPUTypes.TIMING, 1, ISA.ARM)
my_cache = MESITwoLevelCacheHierarchy(
    "32KiB",
    8,
    "32KiB",
    8,
    "256KiB",
    16,
      1)

my_memory = SingleChannelDDR4_2400()
my_board = SimpleBoard("3GHz", my_processor, my_memory, my_cache)

my_board.set_workload(obtain_resource("arm-gapbs-bfs-run"))

my_simulator = Simulator(my_board)
my_simulator.run()
