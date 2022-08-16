""" The essence of the game is to guess the hidden word, you have only four tries to guess, otherwise you lose :) """

secret_word = "frog"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")
