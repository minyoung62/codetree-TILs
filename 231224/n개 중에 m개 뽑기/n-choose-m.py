n, m = map(int, input().split())
a = [ i for i in range(1, n + 1)]
selected = []

def choose(cur_index, cnt):
    if cur_index == n:
        if cnt == m:
            for i in range(n):
                if selected[i] == 1:
                    print(i + 1, end= " ")
            print()
        return
    
    selected.append(1)
    choose(cur_index + 1, cnt + 1)
    selected.pop()

    selected.append(0)
    choose(cur_index + 1, cnt)
    selected.pop()







choose(0, 0)