command = input()

n = len(command)

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
x, y = 0, 0
dx, dy = 3, 3
for c in command:
    if c == 'L':
        dx = (dx + 3) % 4
        dy = (dy + 3) % 4
    elif c == 'R':
        dx = (dx + 1) % 4
        dy = (dy + 1) % 4
    else:
        x += dxs[dx]
        y += dys[dy]

print(x, y)