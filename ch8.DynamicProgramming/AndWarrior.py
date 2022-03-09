N = int(input())

K = list(map(int, input().split()))

dp = [0] * (N)

for i in range(0, N):
    if i == 0:
        dp[0] = K[0] # 맞음
    if i == 1:
        dp[1] = max(K[0], K[1]) # 맞음
    if i == 2:
        dp[2] = max(dp[0]+dp[2], dp[1]) 
    if i >= 3:
        dp[i] = dp[i-2] + K[i]

print(dp[N-1])

# 00:10:50
# 테스트 케이스가 1개 밖에 없다

# 틀린것 같다