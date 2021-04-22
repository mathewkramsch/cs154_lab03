# lab03_q3.py

### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# for testing
def get_expected_output(cycle):
    input_val = ''
    if (sim_trace.trace['s'][cycle]==0): input_val = 'a'
    elif (sim_trace.trace['s'][cycle]==1): input_val = 'b'
    elif (sim_trace.trace['s'][cycle]==2): input_val = 'c'
    elif (sim_trace.trace['s'][cycle]==3): input_val = 'd'
    elif (sim_trace.trace['s'][cycle]==4): input_val = 'e'
    return sim_trace.trace[input_val][cycle]


# Declare data inputs
a = pyrtl.Input(bitwidth=3, name='a')
b = pyrtl.Input(bitwidth=3, name='b')
c = pyrtl.Input(bitwidth=3, name='c')
d = pyrtl.Input(bitwidth=3, name='d')
e = pyrtl.Input(bitwidth=3, name='e')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
o = pyrtl.Output(bitwidth=3, name='o')

# Describe your 5:1 MUX implementation
with pyrtl.conditional_assignment:
    with s == 0:
        o |= a
    with s == 1:
        o |= b
    with s == 2:
        o |= c
    with s == 3:
        o |= d
    with s == 4:
        o |= e

# Simulate and test your design for 16 cycles using random inputs
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
expected_output = 0
for cycle in range(16):
    sim.step({
        'a': random.choice([0,7]),
        'b': random.choice([0,7]),
        'c': random.choice([0,7]),
        'd': random.choice([0,7]),
        'e': random.choice([0,7]),
        's': random.choice([0,4])
    })
    assert(sim_trace.trace['o'][cycle]==get_expected_output(cycle))

print ('--- 3-bit 5:1 MUX Simulation ---')
sim_trace.render_trace()
