import random


connect_four_score = {'User Wins': 0, 'Computer Wins': 0, 'Cats': 0}


def connect_four_greet():

    print()

    print('Welcome to Connect Four!')

    print('Try to get four of your chips in a row!')

    print()

    print('Place your chip by choosing which column (1-7) you want your chip to fall into.')

    print('Your chips are denoted by "O" while the computer\'s chips are denoted by an "X".')

    print()


def connect_four_coin_toss():

    coin_value = random.randint(0, 1)

    print('We\'ll toss a coin to see who goes first.')

    while True:

        user_guess = input('Input either "heads" or "tales" for your guess: ')

        if user_guess.upper() == 'HEADS':

            user_guess_value = 0

            break

        elif user_guess.upper() == 'TALES':

            user_guess_value = 1

            break

        else:

            print('That input is not "heads" or "tales"!')

            print()

    if user_guess_value == coin_value:

        print('You won the coin toss! That means that you go first!')

        print()

        user_turn_value = 0

    else:

        print('Your guess was incorrect! That means that the computer goes first!')

        print()

        user_turn_value = 1

    return user_turn_value


def board_maker():

    board = []

    board_counter = 42

    while board_counter > 0:

        board.append(' ')

        board_counter -= 1

    return board


def connect_four_gameplay(player_turn, board):

    user_id = 'user'

    user_player_symbol = 'O'

    computer_player_symbol = 'X'

    computer_id = 'computer'

    game_winner = False

    while True:

        if player_turn % 2 == 0:

            while True:

                while True:

                    user_choice = input('Pick which column you want to put your chip into: ')

                    if user_choice.isdigit():

                        if 1 <= int(user_choice) <= 7:

                            user_choice_valid = int(user_choice)

                            print()

                            break

                        else:

                            print('Please enter a number that corresponds to one of the columns.')

                            print()

                    else:

                        print('Please enter a number that corresponds to one of the columns.')

                        print()

                board_updated = position_verifier(user_choice_valid, board, user_id)

                if board_updated[1]:

                    print('This column is full, please pick another column to put your chip in.')

                    print()

                else:

                    break

            board = board_updated[0]

            board_rows = 6

            position_offset = 0

            print('  1   2   3   4   5   6   7')

            print('-' * 29)

            while board_rows > 0:

                print('|', board[0 + position_offset], '|', board[1 + position_offset], '|',
                      board[2 + position_offset], '|', board[3 + position_offset], '|',
                      board[4 + position_offset], '|', board[5 + position_offset], '|', board[6 + position_offset], '|')

                print('-' * 29)

                board_rows -= 1

                position_offset += 7

            game_winner = check_win(board, user_player_symbol, game_winner)

            if game_winner:

                player_win = 1

                break

            cat_counter = 0

            for place in board:

                if place != ' ':

                    cat_counter += 1

            if cat_counter == 42:

                player_win = 0

                break

            player_turn += 1

            print('Your chip was placed!')

            print()

            input('Press "enter" to continue: ')

            print()

        else:

            while True:

                computer_choice_valid = random.randint(1, 7)

                board_updated = position_verifier(computer_choice_valid, board, computer_id)

                if board_updated[1]:

                    pass

                else:

                    break

            board = board_updated[0]

            board_rows = 6

            position_offset = 0

            print('  1   2   3   4   5   6   7')

            print('-' * 29)

            while board_rows > 0:

                print('|', board[0 + position_offset], '|', board[1 + position_offset], '|',
                      board[2 + position_offset], '|', board[3 + position_offset], '|',
                      board[4 + position_offset], '|', board[5 + position_offset], '|', board[6 + position_offset], '|')

                print('-' * 29)

                board_rows -= 1

                position_offset += 7

            game_winner = check_win(board, computer_player_symbol, game_winner)

            if game_winner:

                player_win = 2

                break

            cat_counter = 0

            for place in board:

                if place != ' ':

                    cat_counter += 1

            if cat_counter == 42:

                player_win = 0

                break

            print('The computer placed it\'s chip.')

            print()

            player_turn += 1

            input('Press "enter" to continue: ')

            print()

    return player_win


def position_verifier(player_choice, player_board, player_id):

    column_full = False

    spot_counter = 6

    spot_offset = 0

    if player_choice == 1:

        while spot_counter > 0:

            if player_board[0] != ' ':

                column_full = True

                break

            if player_board[35 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[35 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[35 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 2:

        while spot_counter > 0:

            if player_board[1] != ' ':

                column_full = True

                break

            if player_board[36 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[36 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[36 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 3:

        while spot_counter > 0:

            if player_board[2] != ' ':

                column_full = True

                break

            if player_board[37 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[37 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[37 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 4:

        while spot_counter > 0:

            if player_board[3] != ' ':

                column_full = True

                break

            if player_board[38 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[38 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[38 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 5:

        while spot_counter > 0:

            if player_board[4] != ' ':

                column_full = True

                break

            if player_board[39 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[39 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[39 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 6:

        while spot_counter > 0:

            if player_board[5] != ' ':

                column_full = True

                break

            if player_board[40 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[40 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[40 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    elif player_choice == 7:

        while spot_counter > 0:

            if player_board[6] != ' ':

                column_full = True

                break

            if player_board[41 - spot_offset] == ' ':

                if player_id == 'user':

                    player_board[41 - spot_offset] = 'O'

                    break

                elif player_id == 'computer':

                    player_board[41 - spot_offset] = 'X'

                    break

            else:

                spot_offset += 7

                spot_counter -= 1

    return player_board, column_full


def check_win(board, player_symbol, winner_id):

    # Checking the rows

    row_counter = 6

    main_row_offset = 0

    while row_counter > 0:

        row_offset = 0

        while row_offset < 4:

            if (board[0 + main_row_offset + row_offset] == board[1 + main_row_offset + row_offset] ==
                    board[2 + main_row_offset + row_offset] == board[3 + main_row_offset + row_offset] ==
                    player_symbol):

                winner_id = True

                break

            else:

                row_offset += 1

        if winner_id:

            break

        else:

            main_row_offset += 7

            row_counter -= 1

    # Checking the columns

    column_counter = 7

    main_column_offset = 0

    while column_counter > 0:

        column_offset = 0

        while column_offset <= 14:

            if (board[0 + column_offset + main_column_offset] == board[7 + column_offset + main_column_offset] ==
                    board[14 + column_offset + main_column_offset] == board[21 + column_offset + main_column_offset] ==
                    player_symbol):

                winner_id = True

                break

            else:

                column_offset += 7

        if winner_id:

            break

        else:

            main_column_offset += 1

            column_counter -= 1

    # Checking Diagonals #

    # Checking upper right diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[3 + diagonal_counter] == board[9 + diagonal_counter] == board[15 + diagonal_counter] ==
                board[21 + diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    # Checking upper left diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[3 - diagonal_counter] == board[11 - diagonal_counter] == board[19 - diagonal_counter] ==
                board[27 - diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    # Checking bottom right diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[35 + diagonal_counter] == board[29 + diagonal_counter] == board[23 + diagonal_counter] ==
                board[17 + diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    # Checking bottom left diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[41 - diagonal_counter] == board[33 - diagonal_counter] == board[25 - diagonal_counter] ==
                board[17 - diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    # Checking mid-right diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[28 + diagonal_counter] == board[22 + diagonal_counter] == board[16 + diagonal_counter] ==
                board[10 + diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    # Checking mid-left diagonals

    diagonal_counter = 0

    while diagonal_counter <= 3:

        if (board[34 - diagonal_counter] == board[26 - diagonal_counter] == board[18 - diagonal_counter] ==
                board[10 - diagonal_counter] == player_symbol):

            winner_id = True

            break

        else:

            diagonal_counter += 1

    return winner_id


def connect_four_replay(winner):

    if winner == 0:

        print('The game is a tie, so it\'s a Cat!')

        print()

        connect_four_score['Cats'] += 1

    elif winner == 1:

        print('Congrats! You won the game!')

        print()

        connect_four_score['User Wins'] += 1

    elif winner == 2:

        print('The computer won the game!')

        print()

        connect_four_score['Computer Wins'] += 1

    print('Here is the score: ')

    print(connect_four_score)

    print()

    while True:

        replay = input('Would you like to play again? ("Yes"/"No"): ')

        if replay.upper() == 'YES':

            print('Okay, let\'s play again!')

            x = 60

            while x > 0:

                print()

                x -= 1

            break

        elif replay.upper() == 'NO':

            print('Okay, good game!')

            exit()

        else:

            print('Please type either "Yes" or "No".')

            print()


connect_four_greet()

while True:

    first_player = connect_four_coin_toss()

    game_board = board_maker()

    game_winner_number = connect_four_gameplay(first_player, game_board)

    connect_four_replay(game_winner_number)
