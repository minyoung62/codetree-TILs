k, n = tuple(map(int, input().split()))

selected = [0] * n

def choose(cnt):
    if cnt == n:
        print(*selected)
        return
    else:
        for i in range(1, k + 1):
            if cnt >= 2 and (selected[cnt-2] != i and selected[cnt-1] != i):
                continue
            selected[cnt] = i
            choose(cnt + 1)
            # if cnt == 0 or cnt == 1 or (selected[cnt-2] != i and selected[cnt-1] != i):
            #     selected[cnt] = i
            #     choose(cnt + 1)
            

choose(0)