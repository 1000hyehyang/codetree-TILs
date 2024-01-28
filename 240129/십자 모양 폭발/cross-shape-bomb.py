n = int(input()) # 격자의 크기

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split()))

def destroy(r, c): # r행 c열에 해당하는 숫자 만큼 십자 폭탄을 터트린다
    bomb = grid[r][c]

    for row in range(max(0, r - bomb + 1), min(n, r + bomb)): 
        grid[row][c] = 0

    for col in range(max(0, c - bomb + 1), min(n, c + bomb)):  
        grid[r][col] = 0


def gravity():
    temp = [
        [0] * n
        for _ in range(n)
    ]

    for col in range(n): # 첫 번째 열부터 확인을 시작한다.
        temp_row = n - 1
        for row in range(n - 1, -1, -1): # 열의 맨 아래서부터 위로 올라가면서 확인한다.
            if grid[row][col] != 0: # 만약 비어있는 칸이 아니라면
                temp[temp_row][col] = grid[row][col] 
                temp_row -= 1

    for col in range(n):
        for row in range(n):
            grid[row][col] = temp[row][col]

destroy(r - 1, c - 1)
gravity()

for row in range(n):
    for col in range(n):
        print(grid[row][col], end = ' ')
    print()