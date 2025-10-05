import random
import sys

originalCharacters = "abcdefghijklmnopqrstuvwxyz"

charList = list(originalCharacters)

guesses = 10
score3 = 0
score2 = 0
score4 = 0

random.shuffle(charList)
randomWord = random.sample(charList, 5)
shuffledCharacters = "".join(randomWord)

while (guesses > 0):

  def findCommonCharacters(string1, string2):
      set1 = set(string1)
      set2 = set(string2)
      common_chars = set1.intersection(set2)
      return list(common_chars)
    
  guessedWord = input('Input a 5 letter word: ')
  guessedWordCharacters = list(guessedWord)
  guessedWordCharacters = len(guessedWordCharacters)
  if (guessedWordCharacters != 5):
    sys.exit('Only 5 letter words')

  matches = findCommonCharacters(randomWord, guessedWord)
  print(f'The common characters are {matches}')
  guesses = guesses - 1

  if (guessedWord == randomWord):
        score2 = score2 + 1
        score4 = score4 + guesses
        print('Yay you got the word')
        randomWord = random.sample(charList, 5)
        shuffledCharacters = "".join(randomWord)
    
  if (guesses == 0):
     print(f'The word was {shuffledCharacters}')
     score3 = score2 + score4
     print(f'Your score is {score3}')
if (guesses == 0 and score == 1):
  print('You might be the best wordle player out there')
elif (guesses == 0 and score > 1):
  print('That has to be luck')
