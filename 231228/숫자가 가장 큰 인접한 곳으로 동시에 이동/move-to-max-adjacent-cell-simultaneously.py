n, m, t= tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

marbles = [
    [0] * n
    for _ in range(n)
]

next_marbles = [
    [0] * n
    for _ in range(n)
]

# 구슬이 있는 곳에 1을 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    marbles[x-1][y-1] = 1

dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

def inRange(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def findNextStep(x, y):
    maxNum = 0 
    max_nx = 0
    max_ny = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if inRange(nx, ny) and a[nx][ny] > maxNum:
            maxNum = a[nx][ny]
            max_nx = nx
            max_ny = ny
    return max_nx, max_ny


def move(i, j):
    nx, ny = findNextStep(i, j)
    next_marbles[nx][ny] += 1


def move_marble():

    for i in range(n):
        for j in range(n):
            next_marbles[i][j] = 0

    for i in range(n):
        for j in range(n):
            if marbles[i][j] >= 1:
                move(i, j)
                
    for i in range(n):
        for j in range(n):
            marbles[i][j] = next_marbles[i][j]

def delete_mabel():
    for i in range(n):
        for j in range(n):
            if marbles[i][j] >= 2:
                marbles[i][j] = 0    

def simulation():
    move_marble()

    delete_mabel()


for _ in range(t):
    simulation()
    
ans = 0
for i in range(n):
    for j in range(n):
        if marbles[i][j] == 1:

            ans += 1
print(ans)