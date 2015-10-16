import struct, sys, proto, gensafeprime, discrete_log_proof
a=set([])
p=gensafeprime.generate(1024)
for s in sys.argv[2:]:
    a.add(pow(2,int(s),p))
proto.bank("127.0.0.1", int(sys.argv[1]),a,p)
