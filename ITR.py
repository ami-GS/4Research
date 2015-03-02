from math import *
import sys

args = sys.argv[1:]
N, P, V = [float(k) for k in args]
print N, P, V
#print log(N,2)
#print log(P, 2)
#print (1 - P)*log((1-P)/(N-1), 2)
print V * (log(N, 2) + P*log(P, 2) + (1 - P)*log((1-P)/(N-1), 2))
