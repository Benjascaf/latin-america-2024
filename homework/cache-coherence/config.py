"""
This script creates a simple system with a single ARM processor, a single
channel DDR4 memory and a MESI two level cache hierarchy. The processor is
configured to run the ARM ISA and uses a simple timing-based CPU model. The
system is then run with the BFS workload from the GAPBS benchmark suite.

Note that the output will be the output of the workload (in this case BFS) and
the gem5 simulator output.

$ gem5-mesi 01-components.py
Generate Time:       0.00462
Build Time:          0.00141
Graph has 1024 nodes and 10496 undirected edges for degree: 10
...
Average Time:        0.00009
"""

import argparse

from .components.boards import HWX86Board
from .components.processors import HWO3CPU
from .components.cache_hierarchies import  HWMESITwoLevelCacheHierarchy
from .components.memories import HWDDR4
from gem5.simulate.simulator import Simulator
#Algorithm 1
from workloads.array_sum_workload import NaiveArraySumWorkload
#Algorithm 2
from workloads.array_sum_workload import ChunkingArraySumWorkload
#Algorithm 3
from workloads.array_sum_workload import NoResultRaceArraySumWorkload
#Algorithm 4
from workloads.array_sum_workload import ChunkingNoResultRaceArraySumWorkload
#Algorithm 5
from workloads.array_sum_workload import NoCacheBlockRaceArraySumWorkload
#Algorithm 6
from workloads.array_sum_workload import ChunkingNoBlockRaceArraySumWorkload


parser = argparse.ArgumentParser()
parser.add_argument("chosen_workload", type=int)
parser.add_argument("num_cores", type=int)
parser.add_argument("xbar_latency", type=int)
args = parser.parse_args()


workload_options = {
    1: NaiveArraySumWorkload,
    2: ChunkingArraySumWorkload,
    3: NoResultRaceArraySumWorkload,
    4: ChunkingNoResultRaceArraySumWorkload,
    5: NoCacheBlockRaceArraySumWorkload,
    6: ChunkingNoBlockRaceArraySumWorkload
}
# Here we setup a MESI Two Level Cache Hierarchy.
cache_hierarchy = HWMESITwoLevelCacheHierarchy(
    xbar_latency=args.xbar_latency
)

# Setup the system memory.
memory = HWDDR4()

# Create a processor that runs the Arm ISA, has 1 cores and uses a simple
# timing-based CPU model.
processor = HWO3CPU(num_cores=args.num_cores)

# Create a simple board with the processor, memory and cache hierarchy.
board = HWX86Board(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

# Set the workload to run the ARM NPB LU benchmark with size S.
board.set_workload(workload_options[args.chosen_workload](32768, args.num_cores))

# Create a simulator with the board and run it.
simulator = Simulator(board=board)
simulator.run()
