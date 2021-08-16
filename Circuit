from dwavebinarycsp.factories.csp.circuits import multiplication_circuit
import neal

csp = multiplication_circuit(3)
bqm = dwavebinarycsp.stitch(csp)
bqm.fix_variable('a0', 1); bqm.fix_variable('a1', 0); bqm.fix_variable('a2', 1)
bqm.fix_variable('b0', 1); bqm.fix_variable('b1', 1); bqm.fix_variable('b2', 0)
sampler = neal.SimulatedAnnealingSampler()
response = sampler.sample(bqm)
p = next(response.samples(n=1, sorted_by='energy'))

print(p['p5'], p['p4'], p['p3'], p['p2'], p['p1'], p['p0']) 
