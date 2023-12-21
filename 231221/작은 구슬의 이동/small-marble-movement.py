n, t = map(int, input().split())

x, y, dirt = input().split()

cur_dir = 0
if dirt == 'R':
    cur_dir = 0
elif dirt == 'D':
    cur_dir = 1
elif dirt == 'U':
    cur_dir = 2
else:
    cur_dir = 3

x = int(x) - 1 
y = int(y) - 1

c_t = 0 

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def inRange(nx, ny):
    return 0 <= nx < n and 0 <= ny <n

for _ in range(t):
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    if inRange(nx, ny):
        x, y = nx, ny
    else:
        cur_dir = 3 - cur_dir

print(x + 1, y + 1)