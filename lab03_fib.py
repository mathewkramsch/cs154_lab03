# lab03_fib.py
# Simulation of a state machine that computes the nth Fibonacci number after n cyces

import pyrtl
import random

def getNthFibNum(a, b, n):
    """
        Precondition: a,b = 1st,2nd terms of the sequence
        Postcondition: returns the nth term of the Fibonacci Sequence
    """
    if (n==0): return a
    if (n==1): return b
    return getNthFibNum(a,b,n-1) + getNthFibNum(a,b,n-2)

# Inputs and Outputs
A = pyrtl.Input(bitwidth=32,name='A')  # 1st starting terms of the fib sequence
B = pyrtl.Input(bitwidth=32,name='B')  # 2nd starting term (instead of seq. starting w/ 0 & 1)
result = pyrtl.Output(bitwidth=32,name='result')

# updates the value of A and B for each cycle
# for each cycle, result should be A + B 
a_reg = pyrtl.Register(bitwidth=32,name='a_reg')
b_reg = pyrtl.Register(bitwidth=32,name='b_reg')

# Set Register Values (if val==0, then registers != been set yet)
with pyrtl.conditional_assignment:
    with a_reg + b_reg == 0:
        a_reg.next |= A
        b_reg.next |= B
    with a_reg + b_reg != 0:
        a_reg.next |= b_reg
        b_reg.next |= a_reg + b_reg
        
result <<= b_reg



# Simulate and Test
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
for cycle in range(15):
    sim.step({
        'A': 1,
        'B': 1
    })

#sim.step_multiple(sim_inputs)
sim_trace.render_trace()

exit(0)
