ini = (0,1,0,0,1)
p = len(ini)
q = 2

seq = [c for c in ini]
T = 2**p - 1

for i in range(p, T):
    seq.append(seq[i-p] ^ seq[i-q])

NUM = len(seq)
seqStr = "".join([str(c) for c in seq])
print NUM, seqStr

for i in range(len(seq)-p):
    #print seqStr[i:i+5]
    if seqStr.count(seqStr[i:i+5]) > 1:
        print(seqStr.count(seqStr[i:i+5]), seqStr[i:i+5])
        print("This p = %d and q = %d is not suitable for m-sequence" % (p, q))

for i in range(0, NUM, NUM/4):
    print "{" + "".join(["HIGH, " if c == "1" else "LOW, " for c in seqStr[i:] + seqStr[:i]])[:-2] + "}"
    print len(seqStr[i:] + seqStr[:i]), seqStr[i:] + "::" + seqStr[:i]

