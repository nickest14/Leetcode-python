def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n-1, A, C, B)
        print(f'{A} to {C}')
        hanoi(n-1, B, A, C)


n = input("請輸入整數：")
hanoi(int(n), 'A', 'B', 'C')
