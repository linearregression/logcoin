import struct, sys, proto
print "transacted" if proto.wallet(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])) else ""
