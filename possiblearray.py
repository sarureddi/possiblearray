n1=int(input())
m1=list(map(int,input().split()))
x1=y1=u1=k1=0

for i1 in range(0,n1-1):
    if i1==0:
        x1=(x1+m1[i1])/(i1+1)
    else:
        x1=0
        for t1 in range(0,i1):
            x1=x1+m1[t1]
        x1 = (x1 + m1[i1]) // (i1 + 1)
    k1=0
    for j1 in range(i1+1,n1):
        y1=y1+m1[j1]
        k1=k1+1
        if j1==n1-1:
            y1=y1//(k1)
    if x1==y1:
        u1=1
        print("yes")
if u1==0:
    print("no")
