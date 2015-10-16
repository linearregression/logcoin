# logcoin
A toy crypto-currency based on a discrete logarithm zero-knowledge protocol, in &lt;95 lines.

The way logcoin works is as follows:

- A coin C consists of an integer private key x, and a public key $2^{x} mod p$, where p is a very large safe prime.
- The public keys of all coins in circulation are stored in a list on the central tracker.
- Every time a transaction occurs, the following happens:
     1. Alice shares the secret key, via a secure offline channel, with Bob.
     2. Bob generates two random signatures, b and c.
     3. Bob transmits $f_1=2^(x+b) mod p$, $f_2=2^(x+c) mod p$, and $f_3=2^(b+c) mod p$ to the tracker.
     4. The tracker verifies that there exists a coin with pubkey y s.t. $f_1 f_2 mod p = ( (f_3 y) mod p ) y mod p.$
     5. Bob proves knowledge of x and x+b+c using an interactive zero-knowledge protocol based on the discrete log.
     6. The tracker updates the coin's pubkey to $y (f_3) mod p$.  The private key is now (x+b+c)%(p-1), which only Bob knows because he generated b and c.

Note that we protect against double-spending without a blockchain and have a fully anonymous and totally zero-knowledge proof-of-stake system (since only random numbers are transmitted to the tracker).
The reason we have to use two signatures and add them together is to prevent a man-in-the-middle attack.  Let's say we sent only two quantities, $2^(x) mod p$ and $2^(y) mod p$, then an interloper could spoof only the signature and invalidate the coin so Bob cannot spend it. 

To run it, you will need Python 2.7 with generatesafeprime (which is on PIP).
Usage is:

python tracker.py <PORT> <x1> <x2> <x3> <x4> ... <xn>

where x1,x2,x3,x4,etc. are initial secret keys of coins to put into circulation (you also have to distribute them to people; they will be updated securely as soon as they are spent once).

On the other end, you must do:

python wallet.py <IP> <PORT> <x1>

where x1 is the current private key of the coin you want to claim ownership of.

It should be that the wallet prints the new private key of the coin every time it works and otherwise gives no output and an error code of -1.
Transaction time on localhost is 5 or 6 seconds on my machine.  The data transfer is well under 1mb so it shouldn't lag too much more over a network assuming the tracker is centralized.
