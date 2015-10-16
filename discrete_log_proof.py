from math import *
def dexp(p,g,x):
	k=floor(log(p)/log(2))
	b=g if (log(p)-k*log(2)>0.5*log(2)) else 1
	y=1
	while k:
		y=(y*y)%p
		k-=1
	return (y*b)%p;#we choose the integers mod p under addition mod p as our group.
def dlog_know(x,r,p,g,which):
	if which:
		return dexp(p-1,g,x+r)
	return r
def dlog_verify(C,res,y,p,g,which):
	if which:
		return (dexp(p,g,res)==((C*y)%p))
	return (dexp(p,g,res) == C)
def proto_exchange_verify(g,p,y,prng,send,recv,thresh):
	while thresh>0:
		send(2)
		which=(prng()%2)
		C=recv()
		send(which)
		res=recv()
		if not dlog_verify(C,res,y,p,g,which):
			send(31)
			return False
		thresh-=1
	send(32)
	return True
def proto_exchange_prove(g,p,x,prng,send,recv):
	q=2
	while(q==2):
		q=recv()
		if(q!=2):
			break
		r=prng()
		send(dexp(p,g,r))
		which=recv()
		send(dlog_know(x,r,p,g,which))
	return (q==32)
