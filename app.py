the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# print_board(the_board)

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        print_board(the_board)
        print("نوبت شماست" + turn + "به کدام قسمت میخواید حرکت کنید؟")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("این قسمت قبلا پر است.\n به کدام قسمت میخواید حرکت کنید")
            continue