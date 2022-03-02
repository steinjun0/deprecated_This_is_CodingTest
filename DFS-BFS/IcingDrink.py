import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))

ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))

visited = [[False for _ in range(M)] for _ in range(N)]


def search(pos, visited, icecream_count):
    visited[pos[0]][pos[1]] = icecream_count
    for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if pos[0]+diff[0] >= 0 and pos[0]+diff[0] < N:
            if pos[1]+diff[1] >= 0 and pos[1]+diff[1] < M:
                if visited[pos[0]+diff[0]][pos[1]+diff[1]] == False and ice_map[pos[0]+diff[0]][pos[1]+diff[1]] == 0:
                    search((pos[0]+diff[0], pos[1]+diff[1]),
                           visited, icecream_count)


icecream_count = 1

for i_index, i in enumerate(ice_map):
    for j_index, j in enumerate(i):
        if ice_map[i_index][j_index] != 1 and visited[i_index][j_index] == False:
            search((i_index, j_index), visited, icecream_count)
            icecream_count += 1

print(icecream_count-1)


# 47:00
