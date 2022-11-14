from random import randint


def int_input(prompt, error_msg):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            if error_msg:
                print(error_msg)
            continue


def player_turn(player_name, pencils):
    removed = int_input("{}'s turn:\n".format(player_name), "")
    while 1 > removed or removed > 3:
        removed = int_input("Possible values: '1', '2' or '3'\n", "")
    while removed > pencils:
        removed = int_input("Too many pencils were taken\n", "")
    return removed


def has_advantage(pencils):
    return pencils % 4 != 1


def best_move(pencils):
    return (pencils % 4 - 1) % 4


def bot_turn(player_name, pencils):
    max_value = 3 if pencils >= 3 else pencils
    removed = best_move(pencils) if has_advantage(pencils) else randint(1, max_value)
    print("{}'s turn:".format(player_name))
    print(removed)
    return removed


def game(players_list):
    while True:
        pencils = int_input("How many pencils would you like to use:\n",
                            "The number of pencils should be numeric")
        if pencils < 0:
            print('The number of pencils should be numeric')
            continue
        elif pencils == 0:
            print('The number of pencils should be positive')
            continue
        else:
            break

    first_player = input('Who will be the first ({}, {}):\n'.format(players[0], players[1]))
    while first_player not in players_list:
        first_player = input('Choose between {} and {}\n'.format(players[0], players[1]))

    current_player_index = 0 if first_player == players_list[0] else 1

    while pencils > 0:
        print(pencils * "|")
        if current_player_index == 0:
            pencils -= player_turn(players_list[0], pencils)
        else:
            pencils -= bot_turn(players_list[1], pencils)
        current_player_index = (current_player_index + 1) % 2

    print("{} won!".format(players_list[current_player_index]))


if __name__ == '__main__':
    players = ['John', 'Jack']
    game(players)
