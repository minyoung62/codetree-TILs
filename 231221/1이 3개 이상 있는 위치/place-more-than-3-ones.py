n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0 ,-1, 0]

ans = 0

def inRange(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            
            nx, ny = x + dx, y + dy

            if inRange(nx, ny) and a[nx][ny] == 1:
                cnt += 1
   
        if cnt >= 3:
            ans += 1

print(ans)