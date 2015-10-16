import struct, sys, proto, gensafeprime, discrete_log_proof
p=gensafeprime.generate(1024)
coins=set([pow(2,int(s),p) for s in sys.argv[2:]])
proto.bank("127.0.0.1", int(sys.argv[1]),coins,p)
