command = input()

n = len(command)

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]
x, y = 0, 0
curr_dir = 3
for c in command:
    if c == 'L':
        curr_dir = (curr_dir + 3) % 4
    elif c == 'R':
        curr_dir = (curr_dir + 1) % 4
    else:
        x += dxs[curr_dir]
        y += dys[curr_dir]

print(x, y)