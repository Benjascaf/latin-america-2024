
from gem5.isas import ISA
from m5.objects import RiscvO3CPU
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from gem5.components.processors.base_cpu_core import BaseCPUCore

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

class SmallProcessor(BaseCPUProcessor):
    def __init__(self):
        super.__init__([SmallCore()])
