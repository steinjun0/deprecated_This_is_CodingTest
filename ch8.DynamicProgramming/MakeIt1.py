from collections import deque

X = int(input())

def bfs():
    queue = deque()
    queue.append(X)
    queue.append('*')
    step = 0
    while queue:
        num = queue.popleft()
        if num == '*':
            step += 1
            queue.append('*')
            continue

        if num == 1:
            print(step)
            break

        if num > 1:
            if num % 3 == 0:
                queue.append(num/3)
            
            if num % 2 == 0:
                queue.append(num/2)
            
            queue.append(num - 1)
            

bfs()

# 00:10:55
# bfs로 풀었음
# 이게 dp가 맞나?

