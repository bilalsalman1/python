# Building a Guessing Game

secret_word = "Monkey"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Out of guesses ,You Lose!')
else:
    print("You guessed it right! The secret word is:", secret_word)