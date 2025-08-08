import math
n = int(input())
for _ in range (n):
    a,b,c= map(int,input().split())
    d=int(b*c)
    e=int(a/d)
    if a%d==0:
        print(e)
    else:
        print (e+1)
            
