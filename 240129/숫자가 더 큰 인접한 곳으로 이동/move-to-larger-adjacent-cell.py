n, r, c = tuple(map(int, input().split())) # n = 격자의 크기, (r, c) = 시작 위치

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y): # 격자 안에 들어와 있나 확인하자.
    return 0 <= x < n and 0 <= y < n

def simulate(cur_x, cur_y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

    max_num = matrix[cur_x][cur_y]
    max_pos = (-1, -1)

    cnt = 0 # 상 하 좌 우에 갈 수 있는 곳이 아무 곳도 없는지 확인하기 위함

    print(max_num, end = ' ')
    
    while cnt != 4:
        cnt = 0
        for dx, dy in zip(dxs, dys): # 우선순위대로 먼저 살펴본다. 
            next_x, next_y = cur_x + dx, cur_y + dy

            if in_range(next_x, next_y) and matrix[next_x][next_y] > max_num:
                max_num = matrix[next_x][next_y]
                max_pos = (next_x, next_y)
                cur_x, cur_y = max_pos
                print(max_num, end = ' ')
                break
            else:
                cnt += 1
               
simulate(r - 1, c - 1)