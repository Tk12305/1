import random

win = False

def making_a_guess():
    global win
    X = 0
    global update_display, win
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[X]:
            blank[X] = guess.lower()
            correct_guess = True
            if list(blank) == chosen_word:
                win = True
        X += 1
    if not correct_guess:
        print("There is no {guess}, sorry.")
        update_display += 1
    X = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD_LIST = ["Python", "Java", "Javascript", "C#", "C++"]

chosen_word = list(random.choice(WORD_LIST))

blank = "_" * len(chosen_word)

update_display = 0

print(HANGMANPICS[update_display])
guess = input("Welcome to hangman Make a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(list(blank)))
while update_display < 6:
    if blank == chosen_word:
        print("YOU WIN!")
        #WIN VARIABLE
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(''.join(list(blank)))
if update_display == 6:
    print("GAME OVER.") 