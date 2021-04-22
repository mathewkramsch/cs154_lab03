# lab03_fib.py
# Simulation of a state machine that computes the nth Fibonacci number after n cyces

import pyrtl
import random

# Inputs and Outputs
A = pyrtl.Input(bitwidth=32,name='A')  # 1st starting terms of the fib sequence
B = pyrtl.Input(bitwidth=32,name='B')  # 2nd starting term (instead of seq. starting w/ 0 & 1)
result = pyrtl.Output(bitwidth=32,name='result')

# updates the value of A and B for each cycle
a_reg = pyrtl.Register(bitwidth=32,name='a_reg')
b_reg = pyrtl.Register(bitwidth=32,name='b_reg')

# Set Register Values (default register value is 0)
with pyrtl.conditional_assignment:
    with a_reg + b_reg == 0:  # if regs = 0, then havent been set yet
        a_reg.next |= A
        b_reg.next |= B
    with a_reg + b_reg != 0:
        a_reg.next |= b_reg
        b_reg.next |= a_reg + b_reg
        
result <<= b_reg  # result should be sum of a,b registers for each cycle

# Simulate and Test
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(15):
    sim.step({
        'A': 1,
        'B': 1
    })
sim_trace.render_trace()

exit(0)
