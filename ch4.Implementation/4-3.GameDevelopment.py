# 29:05
# DFS 문제네
# 캐릭터가 방문한 칸의 수를 출력하는 프로그램
# N >= 3, M <=50
# (A, B) d => A B d 로 주어진다
# 0: 육지, 1: 바다
# 북 동 남 서
# 0  1  2  3 (북쪽에서 시계방향)

n, m = map(int, input().split())
a, b, d = map(int, input().split())

map_data = []
for i in range(m):
    map_data.append(list(map(int, input().split())))

# map_data[a][b] 에서 시작한다.

step = 0

def search(i, j):
    global step
    while True:
        if map_data[i-1][j] == 0:
            map_data[i-1][j] = 2
            step += 1
            search(i-1, j)
        if map_data[i][j+1] == 0:
            map_data[i][j+1] = 2
            step += 1
            search(i, j+1)
        if map_data[i+1][j] == 0:
            map_data[i+1][j] = 2
            step += 1
            search(i+1, j)
        if map_data[i][j-1] == 0:
            map_data[i][j-1] = 2
            step += 1
            search(i, j-1)
        return


search(a, b)

print(step)