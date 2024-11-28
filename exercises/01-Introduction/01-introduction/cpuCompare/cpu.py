from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory import SingleChannelDDR4_2400
my_atomic_processor = SimpleProcessor(cpu_type=CPUTypes.ATOMIC, num_cores=1, isa=ISA.RISCV)

my_timing_processor = SimpleProcessor(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)

my_minor_processor = SimpleProcessor(cpu_type=CPUTypes.MINOR, num_cores=1, isa=ISA.RISCV)

my_03_processor = SimpleProcessor(cpu_type=CPUTypes.O3, num_cores=1, isa=ISA.RISCV)

my_simple_board = SimpleBoard(
    clk_freq="3GHz",
    processor=my_03_processor,
    memory=SingleChannelDDR4_2400(),
    cache_hierarchy=PrivateL1CacheHierarchy(
        "32KiB",
        "32KiB"
    )
)

workload = obtain_resource("riscv-matrix-multiply-run")
my_simple_board.set_workload(workload=workload)
simulator = Simulator(my_simple_board)
simulator.run()
