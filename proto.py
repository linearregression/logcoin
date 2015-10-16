import gensafeprime,struct,os,socket,math,discrete_log_proof
def mkproto(ip, port,s):
    if s is not None:
        s.listen(1)
        conn,addr=s.accept()
    else:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((ip, port))
    def send(i):
        conn.send(format(i,'x'))
    def recv():
        a=conn.recv(2048)
        return int(a,16)
    def prng():
        return int(os.urandom(1024).encode('hex'),16)
    def close():
        conn.close()
    return send,recv,prng,close
def bank(ip,port,coins,p):
    #p=2**607-1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    while 1:
        send,recv,prng,close=mkproto(ip,port,s)
        send(p)
        y2=recv()
        y3=recv()
        y4=recv()
        y=0
        valid=False
        for coin in coins:
            if (((y4*coin)%p)*coin)%p==(y2*y3)%p:
                y=coin
                print "coin", y
                valid=True
                break
        if valid:
            if discrete_log_proof.proto_exchange_verify(2,p,(y*y4)%p,prng,send,recv,100):
                    coins.remove(y)
                    coins.add((y*y4)%p)
                    print "transacted"
        close()
def wallet(ip,port,x):
    send,recv,prng,close=mkproto(ip,port,None)
    p=recv()
    b=prng()
    send(pow(2,x+b,p))
    c=prng()
    send(pow(2,x+c,p))
    send(pow(2,b+c,p))
    res=discrete_log_proof.proto_exchange_prove(2,p,(x+b+c)%(p-1),prng,send,recv)
    close()
    return res,(x+b+c)%(p-1)
