#ROCK PAPER SCISSORS GAME
import random

players_input = {"R": "Rock", "P": "Paper", "S":"Scissors"}
players_options = list(players_input.keys())

def main():
    player_choice = ""
    while player_choice not in players_options:
        player_choice = input("Make a selection: 'P' for paper, 'S' for scissors or 'P' for paper -> ").upper()
        if player_choice not in players_options:
            print ("Error! Try again...")
    CPU_choice = random.choice(players_options)
    print (f"Player ({players_input[player_choice]}) : CPU ({players_input[CPU_choice]})")
    game_rules(player_choice, CPU_choice)


def game_rules(player, CPU):
    if player == CPU:
        print ("It's a tie! Play again!")
        main()
    elif player == "P":
        if CPU == "R":
            print ("You win!!!")
        else:
            print ("You lose")
    elif player == "S":
        if CPU == "P":
            print ("You win!!!")
        else:
            print ("You lose")
    elif player == "R":
        if CPU == "S":
            print ("You win!!!")
        else:
            print ("You lose")
    return
main()





