import random

min_roll = 1
max_roll = 6


def roll():
    return random.randint(min_roll, max_roll)


while True:
    players = input("Enter the number of players(2-4): ")
    if not players.isdigit():
        print("Enter a integer.")
    else:
        players = int(players)
        if 2 <= players <= 4:
            # print(f"The number of players is {players}.")
            break
        else:
            print("Enter a number between 2 and 4.")

player_num = [0 for _ in range(players)]
max_points = 50

while max(player_num) < max_points:
    for i in range(players):
        current_points = 0
        print("\n\n")
        print(f"Its is turn of player {i+1}.")
        while True:
            ques = input("Do you want to roll(y/n): ")
            if ques.lower() != "y":
                print("\n")
                break
            value = roll()
            if value == 1:
                print("You rolled a 1!.Your turn is over.")
                current_points = 0
                print(f"Your score are {current_points}.")
                print("\n\n")
                break
            else:
                current_points += value
                print(f"You rolled {value}.")
            print(f"Your current points are: {current_points}.\n")
        player_num[i] += current_points

        print(f"Your total score is {player_num[i]}.")
        print()
        for j in range(0, players):
            print(f"The points of player {j+1} are {player_num[j]}")
        print()
        print(f"The player {player_num.index(max(player_num))+1} is winning with {max(player_num)} points.")

print('\n'*3)
print(f"The winner is player {player_num.index(max(player_num))+1}.")
