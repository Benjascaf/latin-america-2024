from gem5.prebuilt.demo.x86_demo_board import X86DemoBoard
from gem5.simulate.simulator import Simulator
from gem5.resources.resource import obtain_resource

my_board = X86DemoBoard()
my_board.set_workload( obtain_resource(resource_id="x86-ubuntu-24.04-boot-no-systemd"))


sim = Simulator(my_board)
sim.run(20_000_000_000)


