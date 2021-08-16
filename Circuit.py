from collections import defaultdict
import dwavebinarycsp as dbc
import dimod
from dwavebinarycsp.factories.csp.circuits import multiplication_circuit
import neal

csp = multiplication_circuit(3)
bqm = dbc.stitch(csp)

print("Please Enter a number between 1 and 49 inclusive: ")
X=int(input()) #read in the number to be multiplied 
if X <= 49 and X >= 1:
    bX = "{:06b}".format(X)
    print(bX)
print("Please Enter a second number between 1 and 49 inclusive: ")
Q=int(input()) #read in the number to be multiplied
if Q <= 49 and Q >= 1:
    bQ = "{:06b}".format(Q)
    print(bQ)

print(bX[5])

bqm.fix_variable('a0', 1); bqm.fix_variable('a1', 0); bqm.fix_variable('a2', 0)
bqm.fix_variable('b0', 1); bqm.fix_variable('b1', 1); bqm.fix_variable('b2', 0)
sampler = neal.SimulatedAnnealingSampler()
response = sampler.sample(bqm)
p = next(response.samples(n=1, sorted_by='energy'))

print(p['p5'], p['p4'], p['p3'], p['p2'], p['p1'], p['p0']) 


def to_base_ten(sample):
    a = 0
    
    a_vars = ['a0', 'a1', 'a2','a3', 'a4', 'a5']
    
    for lbl in reversed(a_vars):
        a = (a << 1) | sample[lbl]
        
    return a
