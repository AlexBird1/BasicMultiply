
import dwavebinarycsp as dbc
from dwavebinarycsp.factories.csp.circuits import multiplication_circuit
import neal

csp = multiplication_circuit(3)
bqm = dbc.stitch(csp)

print("Please Enter a number between 1 and 7 inclusive: ")
P=int(input()) #read in the number to be multiplied 
if P <= 49 and P >= 1:
    bP = "{:03b}".format(P)
    print(bP)
print("Please Enter a second number between 1 and 7 inclusive: ")
Q=int(input()) #read in the number to be multiplied
if Q <= 49 and Q >= 1:
    bQ = "{:03b}".format(Q)
    print(bQ)


if bP[2] == "1":
    bqm.fix_variable('a0', 1)
else:
    bqm.fix_variable('a0', 0)
if bP[1] == "1":
    bqm.fix_variable('a1', 1)
else: 
    bqm.fix_variable('a1', 0)
if bP[0] == "1":
    bqm.fix_variable('a2', 1)
else: 
    bqm.fix_variable('a2', 0)

if bQ[2] == "1":
    bqm.fix_variable('b0', 1)
else:
    bqm.fix_variable('b0', 0)
if bQ[1] == "1":
    bqm.fix_variable('b1', 1)
else: 
    bqm.fix_variable('b1', 0)
if bQ[0] == "1":
    bqm.fix_variable('b2', 1)
else: 
    bqm.fix_variable('b2', 0)




sampler = neal.SimulatedAnnealingSampler()
response = sampler.sample(bqm)
p = next(response.samples(n=1, sorted_by='energy'))

final = (p['p5'], p['p4'], p['p3'], p['p2'], p['p1'], p['p0']) 
print(p['p5'], p['p4'], p['p3'], p['p2'], p['p1'], p['p0']) 
num = int(''.join(map(str,final)))
x = int(str(num), 2)
print('The final result is: ' , x)
