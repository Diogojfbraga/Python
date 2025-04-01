import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
]

word_list = ["aardwark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = '_'
game_over = False
correct_letters = []
full_guessed_letters = []
lives = 6

while not game_over:
    # Ask the user to guess a letter
    guess_letter = input('Please choose a letter: ')
    
    # Create a display that shows the guessed letters
    display = ''
    
    # Check if letter exists in the chosen word
    for letter in chosen_word:
        if letter == guess_letter:
            display += guess_letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += placeholder
            
    print(display)

    if guess_letter not in chosen_word:
        if guess_letter in full_guessed_letters:
            print('You already guessed that letter')
        else:
            full_guessed_letters.append(guess_letter)
            lives -= 1
        
        if lives == 0:
            game_over = True
            print("You lost")
        
        print(f'Lives left: {lives}/6')
        print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win")

