import random

def improve():
        if guess in blanks:
                print(f"{guess} is a letter of the hidden word\n")
        else:
                print(f"You've guessed the letter {guess}, that's not in the word.\n")

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
 
      ! WELCOME TO THE HANGMAN GAME !                 
                   ''')

print(logo)
index = 0
n = 0
chosen_word = random.choice(word_list)
print(f"The word has {len(chosen_word)} letters.")
blanks = list('_' * len(chosen_word)) 
lives = 7
demo_lives = 0

print("------------------------------------")
guess = input("Guess a letter : ").lower()
if guess not in chosen_word:
        lives -= 1
if guess not in chosen_word:
                print(stages[lives])
for i in list(chosen_word):
        if i == guess:                 
                index = n
                blanks.pop(index)                               
                blanks.insert(index,guess)
                n += 1
        else:
                n += 1
print(blanks,"\n")
improve()

while '_' in blanks:
        if lives != 0:
                if n > 0:
                        n = 0
                        print("------------------------------------")
                        guess = input("Guess a letter : ").lower()
                        if guess not in chosen_word:
                                lives -= 1
                        if guess not in chosen_word:
                                print(stages[lives])
                        if '_' in blanks:
                                for i in list(chosen_word):                              
                                        if i == guess:                                   
                                                index = n                    
                                                blanks.pop(index)
                                                blanks.insert(index,guess)
                                                n += 1
                                        else:
                                                n += 1
                                print(blanks,"\n") 
                                improve()
                        if not '_' in blanks:
                                print("\nYou Won")
        else:
                print("------------------------------------")
                print("\nYou lose.!")
                print(f"The hidden word was {chosen_word}\n")
                break