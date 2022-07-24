"""Problem
    A Hangman Game On Python is about guessing letters (A-Z) to form the words. If the player guesses the right letter that is within the word, the letter appears at its correct position. The user has to guess the correct word until a man is hung, then the game is over

"""
from pathlib import Path
import random


def random_word():
  p=Path(__file__).with_name("english_words.txt")
  word_list=[w.strip() for w in p.open("r")]
  word=random.choice(word_list)
  return word



def play():
  #secret_word=random_word().upper()
  secret_word=random_word().upper()
  trials=6
  guessed_letters=[]
  guessed_words=[]
  guessed=False
  dashes="_"*len(secret_word)
  while not guessed and trials > 0:
    guess=input("Guess: ").upper()
    if len(guess)==1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed", guess)
      elif guess not in secret_word:
        guessed_letters.append(guess)
        print("Wrong guess", guess, "not in word")
        trials-=1
      else:
          guessed_letters.append(guess)
          print("you guessed correctly", guess, "is in the word")
          dashes_as_list=list(dashes)
          indices= [i for i, letter in enumerate(secret_word) if letter==guess]
          for index in indices:
            dashes_as_list[index]=guess
          dashes="".join(dashes_as_list)
          if "_" not in dashes:
            guessed=True
      
    elif len(guess)==len(secret_word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed", guess)
      elif guess != secret_word:
          guessed_words.append(guess)
          print("Wrong guess")
          trials-=1
      else:
          guessed=True
          dashes=guess
        
            
    else:
      print("sorry you entered a wrong input")
    print(hanging_man(trials))
    print(dashes)
  if guessed:
    print("Congrats, You guessed the secret_word ", secret_word," correctly")
  else:
    print("Sorry you ran out of tries. The secret word was ", secret_word, ", maybe next time.")



def hanging_man(index):
  stages = ['''
  +---+
  |   |           You hanged the man
  |   |             ____________
  O   |            |  \/    \/  |
 /|\  |            |  /\    /\  |
 / \  |            |     *      |
                   |   ------   |
=========          |____________|
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
  return stages[index]

def main():
  print("<!-------------Guess Game--------------->")
  message="""
  Your goal in this game is to guess a secret word before you are hanged.
  You can choose to guess each letter at a  time or guess the secret word once.
  """
  print(message)
  play()
  while True:
    choice=input("Do you want to play again(y/n): ").upper()
    if choice=="Y":
      play()
    elif choice=="N":
      break
    else:
      print("Wrong input!")
if "__main__"==__name__:
  main()