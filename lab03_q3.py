# lab03_q3.py

### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
i0 = pyrtl.Input(bitwidth=3, name='i0')
i1 = pyrtl.Input(bitwidth=3, name='i1')
i2 = pyrtl.Input(bitwidth=3, name='i2')
i3 = pyrtl.Input(bitwidth=3, name='i3')
i4 = pyrtl.Input(bitwidth=3, name='i4')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
out = pyrtl.Output(bitwidth=3, name='out')

# Describe your 5:1 MUX implementation
with pyrtl.conditional_assignment:
    with s == 0:
        out |= i0
    with s == 1:
        out |= i1
    with s == 2:
        out |= i2
    with s == 3:
        out |= i3
    with s == 4:
        out |= i4

# Simulate and test your design for 16 cycles using random inputs
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
expected_output = 0
for cycle in range(16):
    sim.step({
        'i0': random.choice([0,7]),
        'i1': random.choice([0,7]),
        'i2': random.choice([0,7]),
        'i3': random.choice([0,7]),
        'i4': random.choice([0,7]),
        's': random.choice([0,4])
    })
    assert (  # asserts that value in ix, where x=s, == output (per cycle)
            sim_trace.trace[ 'i'+str(sim_trace.trace['s'][cycle]) ][cycle] 
            == sim_trace.trace['out'][cycle] )

print ('--- 3-bit 5:1 MUX Simulation ---')
sim_trace.render_trace()
