k, n= tuple(map(int, input().split()))
selected = [0] * n
def choose(cnt):
    if cnt == n:
        print(*selected)
        return
    
    for i in range(1, k + 1):
        selected[cnt] = i 
        choose(cnt + 1)

choose(0)