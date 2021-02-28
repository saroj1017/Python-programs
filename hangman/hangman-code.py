import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

# clear is module in replit platform you can use other modules to clear the data 

#prints the logo from the module hangman_art
print(logo)

# itiallly sets set a varibale that points to false and upon some trigger inputs the variable is set to True
game_is_finished = False

# number of lives remaining initally 7 - 1 =6 , which displays only the rope of the game
lives = len(stages) - 1

# computer chooses a random word from the module handman_words
chosen_word = random.choice(word_list)

# calculates the length of the random word choosen from computer
word_length = len(chosen_word)

# displays the number of words to the user via the "_" symbol
display = []
for _ in range(word_length):
    display += "_"

# this while loop will keep on running untill game_is_finished varibale changes to True    
while not game_is_finished:
  
    # user inputs a letter to guess @ the starting of the game itself
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    # lets say word is affix , len = 5 
    # so 0 = a , 1 = f , 2 =f , 3 = i , 4 = x
    # lets say i guessed f then first the index 1 matches so the _ is replaced by the corresponding letter
    # same happens for index 2 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    # next guess was p which is not in the word      
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # end of the game as all lives are lost  
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            print("correct answer was" ,chosen_word)
    
    # if all guesses fills the display then your o/p is correct and you win       
    if not "_" in display:
        game_is_finished = True
        print("You win.")
          
    # at each guess you will be displayed the ascii art for the stage you are currenlty in
    print(stages[lives])

          
          
          
# example o/p           
# Note that in the below example output all the asicii arts gets cleared and only the lastest ASCII art remains
'''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Guess a letter: y

# shows how many letters are required to fill the word                                     
_ _ _ _ _
You guessed y, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: p
                                     
_ _ _ _ _
You guessed p, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: s
                                     
_ _ _ _ _
You guessed s, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: a
                                     
# note that no life is taken and the letter o/p is filled at the correct position                                     
a _ _ _ _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: n

# i was guessing angry but that was wrong :)                                      
You guessed n, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========                                                                                                           

Guess a letter: t

You guessed t, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: d

                                     
You guessed d, that's not in the word. You lose a life.
You lose.
correct answer was affix

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========                                     

                                     
'''                                     
                                     
