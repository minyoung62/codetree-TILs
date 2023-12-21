n, m = map(int, input().split())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

cur_dir = 0
cur_num = 1
a = [
    [0] * m
    for i in range(n)
]

a[0][0] = 1
x, y = 0, 0

def inRange(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


for i in range(2, n* m + 1):

    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if not inRange(nx, ny) or a[nx][ny] != 0:
        cur_dir = (cur_dir + 1) % 4
        

    x, y = x + dxs[cur_dir], y + dys[cur_dir]

    a[x][y] = i

for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()