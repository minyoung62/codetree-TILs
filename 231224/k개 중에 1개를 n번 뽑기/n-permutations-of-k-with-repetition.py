k, n= tuple(map(int, input().split()))
selected = []
def choose(cnt):
    if cnt == n:
        print(*selected)
        return
    
    for i in range(1, k + 1):
        selected.append(i)
        choose(cnt + 1)
        selected.pop()

choose(0)