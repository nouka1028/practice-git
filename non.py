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
            ans.pop(ans.index(x[i]))
        
    return h,b


avg=0
for _ in range(100):
    cand=[]
    for i in range(0,10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    cand.append(f"{i}{j}{k}{l}")
    custom_ans=f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    cnt=0
    go=f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    print(go)
    while True:
        # num,rslt=map(str,input().split())
        # h=int(rslt[0])
        # b=int(rslt[1])
        h,b=a(custom_ans,go)
        t=[]
        for i in cand:
            ans=i
            # h_exam,b_exam=a(ans,num)
            h_exam,b_exam=a(ans,go)

            if h_exam==h and b_exam==b:
                t.append(i)
        cand=t[:]
        go=cand[randint(0,len(cand)-1)]
        print(go)
        cnt+=1
        if len(cand)==1:
            break
    print(cnt)
    avg+=cnt
print(avg/100)

    