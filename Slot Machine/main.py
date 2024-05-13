import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}

symbol_values = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}


def deposit():
    while True:
        player_money = input("Enter the money you want to deposit: $")
        if player_money.isdigit():
            player_money = int(player_money)
            if player_money > 0:
                break
            else:
                print("Enter a number greater than zero.")
        else:
            print("Enter a number.")

    return player_money


def get_number_of_lines():
    while True:
        no_of_lines = input(f"Enter the number of line 1-{MAX_LINES}: ")
        if no_of_lines.isdigit():
            no_of_lines = int(no_of_lines)
            if 1 <= no_of_lines <= MAX_LINES:
                break
            else:
                print(f"Enter a number between 1-{MAX_LINES}.")
        else:
            print("Enter a number.")
    return no_of_lines


def get_bet():
    while True:
        bet = input(f"Enter the amount to bet ({MIN_BET}-{MAX_BET}): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between {MIN_BET}-{MAX_LINES}.")
        else:
            print("Enter a number.")
    return bet


def get_slot_machine_spin(rows, columns, symbols):
    all_symbols = []


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if balance < total_bet:
            print(f"You don't have enough balance to bet.Your balance is {balance}.")
        else:
            break

    print(f"You are betting {bet} on {lines} lines.Total bet is {bet*lines}.")


main()
