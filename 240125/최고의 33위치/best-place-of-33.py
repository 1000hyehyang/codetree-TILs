n = int(input())

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

def coin(row_s, col_s, row_e, col_e):
    coins = 0

    for row in range(col_s, col_e + 1):
        for col in range(col_s, col_e + 1):
            coins += matrix[row][col]
        
    return coins
    
max_coin = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_coin = coin(row, col, row + 2, col + 2)

        max_coin = max(max_coin, num_of_coin)

print(max_coin)