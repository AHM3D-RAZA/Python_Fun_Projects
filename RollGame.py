import random

player1_score = 0
player2_score = 0

def play_move():
    global player1_score, player2_score

    player1_up = True
    while True:
        if player1_up:
            print("Player1's Move!")
            player1_score += move()
            print(f"Player 1's Total Score is {player1_score}!")
            if is_winner(player1_score):
                print("Player1 Won! Congrats!!")
                break
            player1_up = False

        else:
            print("Player2's Move!")
            player2_score += move()
            print(f"Player 2's Total Score is {player2_score}!")
            if is_winner(player2_score):
                print("Player1 Won! Congrats!!")
                break
            player1_up = True

    if (input("Want to play another Game? (y/n)").lower().rstrip()) == "y":
        main()
    else:
        print("GoodGame!")
        exit()


def move():
    local_score = 0
    run = True
    while run:
        user_input = input(f"Do you want to Roll the Dice or Stop? (Roll/Stop/q to quit): ").lower().rstrip()
        
        if user_input == "roll":
            roll_random = roll()
            if (roll_random == 1):
                print("Player rolled and got a 1.")
                return 0
            else:
                local_score += roll_random
                print(f"Player rolled and got a {roll_random}. Stacked score is {local_score}")
        elif user_input == "stop":
            print(f"Player stopped. {local_score} added to Player's Total Score.")
            return local_score
        elif user_input == "q":
            print("GoodGame!")
            exit()
        else:
            print("Invalid Input!")

def roll():
    return random.randint(1,6)

def is_winner(score):
    return score >= 50

def main():
    print("""\t\t\t\tGame Rules!\nThe player has two options: To Roll the Dice or stop.
The score keeps stacking until the dice rolls 1.
If you stop rolling before 1 then the stacked score gets added to Player's total score.
If Player keeps rolling and rolls a 1 then the Player loses the stacked score and 0 gets added to the total score.
First one to total score of 50 Wins.\n\t\t\t\tGood Luck!!""")
    play_move()

main()