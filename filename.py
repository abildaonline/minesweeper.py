import random

def create_board(rows, cols, bombs):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    bombs_placed = 0
    while bombs_placed < bombs:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != 'B':
            board[row][col] = 'B'
            bombs_placed += 1
    return board

def print_board(board):
    rows = len(board)
    cols = len(board[0])
    print('   ' + ' '.join([str(i) for i in range(cols)]))
    print('  ' + '---' * cols)
    for i in range(rows):
        print(str(i) + ' |' + '|'.join(board[i]) + '|')
        print('  ' + '---' * cols)

def count_adjacent_bombs(board, row, col):
    count = 0
    rows = len(board)
    cols = len(board[0])
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if board[i][j] == 'B':
                count += 1
    return count

def reveal_square(board, revealed, row, col):
    if revealed[row][col]:
        return
    rows = len(board)
    cols = len(board[0])
    if board[row][col] != 'B':
        bombs = count_adjacent_bombs(board, row, col)
        board[row][col] = str(bombs)
        revealed[row][col] = True
        if bombs == 0:
            for i in range(max(0, row - 1), min(row + 2, rows)):
                for j in range(max(0, col - 1), min(col + 2, cols)):
                    reveal_square(board, revealed, i, j)
    else:
        revealed[row][col] = True

def play_game():
    rows = int(input('Введите количество строк: '))
    cols = int(input('Введите количество столбцов: '))
    bombs = int(input('Введите количество бомб: '))

    board = create_board(rows, cols, bombs)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    first_move = True

    while True:
        print_board(board)
        row = int(input('Введите номер строки: '))
        col = int(input('Введите номер столбца: '))

        if first_move:
            while board[row][col] == 'B':
                # Если первый выбор попал на мину, перегенерируем поле
                board = create_board(rows, cols, bombs)
            first_move = False

        if board[row][col] == 'B':
            print('Вы проиграли!')
            print_board(board)
            break

        reveal_square(board, revealed, row, col)

        all_revealed = True
        for i in range(rows):
            for j in range(cols):
                 if board[i][j] != 'B' and not revealed[i][j]:
                    all_revealed = False
                    break
            if not all_revealed:
                break

        if all_revealed:
            print('Вы выиграли!')
            print_board(board)
            break

play_game()
