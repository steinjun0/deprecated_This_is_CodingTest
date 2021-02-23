# 05:39

n, k = map(int,input().split())
print(n, k)
i = 0
while(True):
  if(n%k != 0):
    n = n-1
  else:
    n = n/k
  i = i+1
  if(n == 1): break

print(i)

# 나누기/곱하기가 뺄셈/덧셈 보다 빠르다 => 나누기/곱셈을 많이 할 생각을 하자(뺄셈/덧셈은 한번에 할 수 있도록)