from math import log
from gem5.components.processors.abstract_generator import AbstractGenerator
from gem5.components.processors.abstract_generator import partition_range

class HybridGenerator (AbstractGenerator):
    def __init__(self):
        self

    def get_num_linear_cores(num_cores: int):
        if (num_cores & (num_cores - 1) == 0):
            return num_cores / 2
        else:
            return 2** int(log(num_cores, 2))
