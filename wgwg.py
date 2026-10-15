t=int(input())
for i in range(t):
    n = int(input())
    q=n
    while n%10!=9:
        n-=1
    ans=(n**2+82*n+81)//20
    for o in range(q,n,-1):
        s = sum(int(a) for a in str(o))
        ans+=s
    print(ans)
