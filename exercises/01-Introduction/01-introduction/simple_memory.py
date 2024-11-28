"""
This script creates a simple system with a traffic generator to test memory

$ gem5 memory-test.py
"""

import argparse
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.boards.test_board import TestBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.simple import SingleChannelSimpleMemory
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.memory.multi_channel import ChanneledMemory
from gem5.components.memory.dram_interfaces.lpddr5 import LPDDR5_6400_1x16_BG_BL32
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.components.processors.random_generator import RandomGenerator
from gem5.simulate.simulator import Simulator
from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import PrivateL1PrivateL2CacheHierarchy
from my_processor import BigProcessor, LittleProcessor

parser = argparse.ArgumentParser()
# parser.add_argument("rate", type=str, help="The rate of the processor")
# parser.add_argument("rd_perc", type=int, help="The read percentage parameter")
# parser.add_argument("generator", type=str, help="The generator to use")
# parser.add_argument("memory_system", type=str, help="The type of memory")
# parser.add_argument("max_addr", type=int, help="The max memory for the generator to generate traffic for")
parser.add_argument("cpu_type", type=str, help="ceada")
args = parser.parse_args()
# my_generator = LinearGenerator(num_cores=1, max_addr=args.max_addr ,rate=args.rate, rd_perc=args.rd_perc) if (args.generator == "Linear")  else RandomGenerator(num_cores=1, max_addr=args.max_addr, rate=args.rate, rd_perc=args.rd_perc)

# def get_memory(mem_type: str):
#     if mem_type == "simple":
#         return SingleChannelSimpleMemory(
#             latency="20ns", bandwidth="32GiB/s", latency_var="0s", size="1GiB"
#         )
#     elif mem_type == "DDR4":
#         return SingleChannelDDR4_2400()
#     elif mem_type == "SC_LPDDR5":
#         return ChanneledMemory(LPDDR5_6400_1x16_BG_BL32, 4, 64)

# my_board = TestBoard(
#     "3GHz",
#     generator= my_generator,
#     memory=get_memory(args.memory_system),
#     cache_hierarchy=PrivateL1PrivateL2CacheHierarchy(l1d_size="32KiB", l1i_size="32KiB", l2_size="256KiB")
# )
# simulator = Simulator(board=my_board)
# simulator.run()

# stats = simulator.get_simstats()
# seconds = stats.simTicks.value / stats.simFreq.value
# total_bytes = (
#     stats.board.processor.cores[0].generator.bytesRead.value
#     + stats.board.processor.cores[0].generator.bytesWritten.value
# )
# latency = (
#     stats.board.processor.cores[0].generator.totalReadLatency.value
#     / stats.board.processor.cores[0].generator.totalReads.value
# )
# print(f"Total bandwidth: {total_bytes / seconds / 2**30:0.2f} GiB/s")
# print(f"Average latency: {latency / stats.simFreq.value * 1e9:0.2f} ns")

if args.cpu_type == "Big":
    processor = BigProcessor()
elif args.cpu_type == "Little":
    processor = LittleProcessor()

board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=SingleChannelDDR4_2400("1GiB"),
    cache_hierarchy=PrivateL1CacheHierarchy(
        l1d_size="32KiB", l1i_size="32KiB"
    ),
)
