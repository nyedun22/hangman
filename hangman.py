import random

# List of words to use in game
from hangman_words import word_list

# Randomly select word from the word_list and assign to a variable
chosen_word = str(random.choice(word_list))
# Create empty list for display and add "_" to match each letter in selected word
display = []
word_length = len(chosen_word)
for letter in range(word_length):
    display += "_"
print(display)

# while loop to let user guess again - while should stop when all letters have been guessed
end_of_game = False
lives = 6

while not end_of_game:
    # Ask user to guess a letter and assign answer to a variable
    letter_guess = input('Guess a letter ').lower()
# check if user has already entered a letter guess and remind them it's already been chosen
    if letter_guess in display:
        print(f'{letter_guess} has already been chosen, please choose a different letter')
# Check if the letter guessed is in the randomly chosen word and replace blank with letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == letter_guess:
            display[position] = letter
# if letter guessed is not in chosen word then player lives reduced -1
    if letter_guess not in chosen_word:
        lives -= 1
        print(f'You have chosen a letter not in the word - you lose a life')
        if lives == 0:
            end_of_game = True
            print(f"You lose! End of game. The selected word was {chosen_word}")

# join elements in list and turn into string
    print(f"{' '.join(display)}")

# ending the loop - user wins the game
    if "_" not in display:
        end_of_game = True
        print("You win the game!")

# import & print stages/visual elements which correspond to number of player lives
    from hangman_art import stages
    print(stages[lives])
