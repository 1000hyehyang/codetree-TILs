n, m, k = tuple(map(int, input().split())) # n: 격자의 크기, m: 가로 블럭의 길이, k: 블록이 떨어질 위치(열)

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx, dy = 1, 0 # 어차피 떨어질 블록의 아랫부분만 1로 채워져 있는지 확인하면 되므로 '하'만 봐준다.

def simulate():
    cur_x, cur_y = 0, k - 1
    cnt = 0

    while cnt == 0:
        for _ in range(m): # 블록의 길이만큼 아래에 뭐가 채워져 있는지 확인한다.
            next_x, next_y = cur_x + dx, cur_y + dy
            if matrix[next_x][next_y] == 0:
                cur_y += 1 # 아래에 뭐가 없으면 다음 블록의 아래를 확인해주자.
            else:
                cnt += 1 # 아래에 뭐가 있으면 카운트를 해주자...
                cur_y = k - 1
                break

        if cnt != 0: # 아래에 뭐가 있다면, 현재 자리에 블록을 채워준다.
            for i in range(m):
                matrix[cur_x][cur_y + i] = 1
            break

        cur_x += 1
        cur_y = k - 1
        cnt = 0

simulate()

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()