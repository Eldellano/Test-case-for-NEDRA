import random


board = a = [['-'] * 3 for i in range(3)]
for i in board:
    print(i)


def move():
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    return x, y


def game():
    player_1 = 'x'  # нечетные ходы
    player_2 = '0'  # четные ходы
    cnt = random.randint(0, 1)  # определяем кто ходит первым
    while True:
        if cnt % 2 != 0:
            # ходит игрок 1
            x, y = move()
            if board[x][y] == '-' and board[x][y] != '0':
                board[x][y] = player_1
                print(f'Игрок player_1 ставит {player_1} на строку "{x + 1}" столбец "{y+ 1}"')
                for i in board:
                    print(i)
                print('---------------')
                if check_win():
                    print('Выиграл игрок 1!!!')
                    break
                cnt += 1
            else:
                continue

        else:
            # ходит игрок 2
            x, y = move()
            if board[x][y] == '-' and board[x][y] != 'x':
                board[x][y] = player_2
                print(f'Игрок player_2 ставит {player_2} на строку "{x + 1}" столбец "{y+ 1}"')
                for i in board:
                    print(i)
                print('---------------')
                if check_win():
                    print('Выиграл игрок 2!!!')
                    break
                cnt += 1
            else:
                continue


def check_win():
    # проверка
    for i in board:
        # строки
        if i.count('x') == 3 or i.count('0') == 3:
            return True
        # диагонали
        elif (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x') \
                or (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x'):
            return True
        elif (board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0') \
                or (board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0'):
            return True
        # вертикали
        else:
            for j in range(3):
                if board[0][j] == 'x' and board[1][j] == 'x' and board[2][j] == 'x':
                    return True
                elif board[0][j] == '0' and board[1][j] == '0' and board[2][j] == '0':
                    return True

    # ничья
    cnt_draw = 0
    for i in board:
        for j in i:
            if j in ('x', '0'):
                cnt_draw += 1
            else:
                cnt_draw = 0
    if cnt_draw == 9:
        print('Ничья')
        raise Exception


if __name__ == "__main__":
    game()
