order = input()

x, y = 0, 0
dir_num = 0
dx = [0, 1, 0, -1] # 북 동 남 서
dy = [1, 0, -1, 0]


for i in order:
    if i == 'L':
        dir_num = (dir_num + 3) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'F':
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

print(nx, ny)