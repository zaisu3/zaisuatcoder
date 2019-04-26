N,W=(int(x) for x in input().split())
t=0
weight=[0]*N
value=[0]*N
while t<N:
    v,w=(int(x) for x in input().split())
    value[t]=v
    weight[t]=w
    t=t+1
def kotae(N,W):
    dp=[[0 for i in range(110)] for j in range(110)]
    i=0
    while i<N:
        wei=0
        while wei<W+1:
            if wei>=weight[i]:
                dp[i+1][wei]=max(dp[i][wei],dp[i][wei-weight[i]]+value[i])
            else:
                dp[i+1][wei]=dp[i][wei]
            wei=wei+1
        i=i+1
    return dp[N][W]
print(kotae(N,W))
