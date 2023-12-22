n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0

def getNum(i, j):
    cnt = 0
    for x in range(i, i + 3):
        for y in range(j,j + 3):
            if a[x][y] == 1:
                cnt += 1
    return cnt


for i in range(n-2):
    for j in range(n-2):
        cnt = getNum(i, j)
        ans = max(ans, cnt)
print(ans)