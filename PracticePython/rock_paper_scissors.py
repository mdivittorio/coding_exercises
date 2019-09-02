def main():
    while True:
        play_a = input("Please enter player 1's choice: ")
        play_b = input("Please enter player 2's choice: ")
        print(get_winner(play_a, play_b))
        play_again = input('Would you like to play again? ')
        if play_again not in ['y', 'yes']:
            break


def get_winner(play_a, play_b):
    if play_a == play_b:
        winning_text = "It's a tie!"
    elif play_a == 'rock':
        if play_b == 'scissors':
            winning_text = 'Player 1 wins!'
        else:
            winning_text = 'Player 2 wins!'
    elif play_a == 'scissors':
        if play_b == 'rock':
            winning_text = 'Player 2 wins!'
        else:
            winning_text = 'Player 1 wins!'
    elif play_a == 'paper':
        if play_b == 'scissors':
            winning_text = 'Player 2 wins!'
        else:
            winning_text = 'Player 1 wins!'
    return winning_text + '\n'


main()
