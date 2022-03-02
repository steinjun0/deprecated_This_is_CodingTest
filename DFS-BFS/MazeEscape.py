import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

map_maze_origin = []

for i in range(N):
    map_maze_origin.append(list(map(int, input())))

# empty_visited = [[False for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# min_step = 999


# def dfs(x, y, step):
#     global min_step
#     if x == M-1 and y == N-1:
#         if step < min_step:
#             min_step = step
#     if x >= 0 and x < M and y >= 0 and y < N and map_maze_origin[y][x] == 1 and visited[y][x] == False:
#         visited[y][x] = True
#         dfs(x+1, y, step+1)
#         dfs(x-1, y, step+1)
#         dfs(x, y+1, step+1)
#         dfs(x, y-1, step+1)


# dfs(0, 0, 0)
# print(min_step+1)


# 19:14 dfs해결


step = 0


def bfs(x, y):
    # x, y = dq.popleft()
    # visited[y][x] = True
    dq = deque([(x, y, 0)])
    while len(dq) > 0:
        x, y, step = dq.popleft()
        if x == M-1 and y == N-1:
            return step+1
        for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            diff_x = diff[0] + x
            diff_y = diff[1] + y
            if diff_x >= 0 and diff_x < M and diff_y >= 0 and diff_y < N and map_maze_origin[diff_y][diff_x] == 1 and visited[diff_y][diff_x] == False:
                visited[diff_y][diff_x] = True
                dq.append((diff_x, diff_y, step + 1))


print(bfs(0, 0))

# 56:41 bfs해결(37:26)
