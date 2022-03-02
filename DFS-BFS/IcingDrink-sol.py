import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))

ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or ice_map[y][x] == 1:
        return False
    else:
        ice_map[y][x] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True


result = 0
for i_index, i in enumerate(ice_map):
    for j_index, j in enumerate(i):
        if dfs(j_index, i_index):
            result += 1

print(result)
