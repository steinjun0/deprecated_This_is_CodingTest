# 21/02/16 18분 57초

N, M = map(int, input().split())

cards = []
for i in range(N):
  cards.append(list(map(int, input().split())))

biggestElem = [10001 for _ in range(N)]
for i in range(N):
  for j in range(M):
    if biggestElem[i] > cards[i][j]:
      biggestElem[i] = cards[i][j]

biggestRow = 0
for i in range(N-1):
  if biggestElem[biggestRow] < biggestElem[i+1]:
    biggestRow = i+1

print(biggestElem[biggestRow])



N, M = map(int, input().split())
result = 0
for i in range(N):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  result = max(result, min_value)

print(result)