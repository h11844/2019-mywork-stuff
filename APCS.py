# coding: utf-8
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
if a!=0:
    a=1
if b!=0:
    b=1
if c!=0:
    c=1
if (a&b==c):
    print("AND")
if (a|b==c):
    print("OR")
if (a^b==c):
    print("XOR")
if not ((a&b==c) or (a|b==c) or (a^b==c)):
    print("IMPOSSIBLE")
