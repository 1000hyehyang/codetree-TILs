n, m = tuple(map(int, input().split())) # n: 격자의 크기, m: 연속해야 하는 숫자의 수

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

happy_row = 0
happy_col = 0

def row_check(n, m):
    global happy_row
    
    if n > 1:
        for i in range(n):
            cnt = 1
            for j in range(1, n):
                if grid[i][j] == grid[i][j-1]:
                    cnt += 1
                else:
                    cnt = 1 

                if cnt >= m:
                    happy_row += 1
                    break
    else:
        cnt = 1
        if cnt >= m:
            happy_row += 1
    
    return happy_row

def col_check(n, m):
    global happy_col
    if n > 1:
        for i in range(n):
            cnt = 1
            for j in range(1, n):
                if grid[j][i] == grid[j-1][i]:
                    cnt += 1
                else:
                    cnt = 1 

                if cnt >= m:
                    happy_col += 1
                    break
    else:
        cnt = 1
        if cnt >= m:
            happy_col += 1   
    
    return happy_col


print(row_check(n, m) + col_check(n, m))