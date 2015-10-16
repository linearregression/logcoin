import struct, sys, proto, gensafeprime, discrete_log_proof
a=set([])
for s in sys.argv[2:]:
    a.add(int(discrete_log_proof.dexp(2,2**607-1,sys.argv[2:])))
proto.bank("127.0.0.1", int(sys.argv[1]),a)
