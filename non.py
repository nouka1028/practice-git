cand=[]
for i in range(0,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                cand.append(f"{i}{j}{k}{l}")
from random import randint

def a(ans,x):
    h=0
    b=0
    ans=list(ans)
    x=list(x)
    g=set()
    for i in range(4):
        if ans[i]==x[i]:
            h+=1
            ans[i]="garbage"
            g.add(i)
    for i in range(4):
        if (x[i] in ans) and (i not in g):
            b+=1
        
    return h,b

while True:
    num,rslt=map(str,input().split())
    h=int(rslt[0])
    b=int(rslt[1])
    t=[]
    for i in cand:
        ans=i
        h_exam,b_exam=a(ans,num)
        if h_exam==h and b_exam==b:
            t.append(i)
    cand=t[:]
    print(cand)
    print(cand[randint(0,len(cand)-1)])
    

    