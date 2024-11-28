
from gem5.isas import ISA
from m5.objects import RiscvO3CPU
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator
from gem5.utils.multisim import multisim
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.boards.simple_board import SimpleBoard
class BigO3(RiscvO3CPU):
    def __init__(self):
        super.__init__()
        self.fetchWidth = 8
        self.decodeWidth = 8
        self.RenameWidth = 8
        self.IssueWidth = 8
        self.wbWidth = 8
        self.CommitIssueWidth = 8

        self.numROBEntries = 256
        self.numIntRegs = 512
        self.numFpRegs = 512

class LittleO3(RiscvO3CPU):
    def __init__(self):
        super.__init__()
        self.fetchWidth = 2
        self.decodeWidth = 2
        self.RenameWidth = 2
        self.IssueWidth = 2
        self.wbWidth = 2
        self.CommitIssueWidth = 2

        self.numROBEntries = 30
        self.numIntRegs = 40
        self.numFpRegs = 40

class BigCore(BaseCPUCore):
    def __init__(self):
        super.__init__(LittleO3(), ISA.RISCV)

class SmallCore(BaseCPUCore):
    def __init__(self):
        super.__init__(LittleO3(), ISA.RISCV)

class BigProcessor(BaseCPUProcessor):
    def __init__(self):
        super.__init__([BigCore()])

    @classmethod
    def get_name(cls):
        return "big"

@classmethod
class SmallProcessor(BaseCPUProcessor):
    def __init__(self):
        super.__init__([SmallCore()])

    def get_name(cls):
        return "little"

multisim.set_num_processes(2)
for processor_type in {BigProcessor, SmallProcessor}:
    for benchmark in obtain_resource("riscv-getting-started-benchmark-suite"):
        board = SimpleBoard(
                            clk_freq="3GHz",
                            processor=processor_type(),
                            memory=SingleChannelDDR4_2400("1GiB"),
                            cache_hierarchy=PrivateL1CacheHierarchy
                                ("32KiB",
                                 "32KiB"
                                )
                            )
        board.set_workload(benchmark)
        simulator = Simulator(board, id=f"{processor_type.get_name()}-{benchmark.get_id()}")
        multisim.add_simulator(simulator)
