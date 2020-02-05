#importing random library to choose random word
import random

#taking list of words 
WORDS = ('apple', 'oracle', 'amazon', 'microsoft' , 'book' , 'google')   

#choosing one of random word
correct_word = random.choice(WORDS)

#taking as clue for giving hint to user first and last character
clue = correct_word[0] + correct_word[-1]

#string for storing letters taken input by user
store_letter = ''

print('Welcome to "Guess the Word Game!"')

#taking input as limit how many chances user want
limit = int(input('Enter How many chances do you want: '))

#showing how many chances u had taken
print('You have %d attempts at guessing letters in a word' % (limit))

print('Let\'s begin!')


for guess_count in range(limit):
    while True:
        letter_guess = input('Guess a letter: ')

        if len(letter_guess) == 1:
            break
        else:
            print("Oops! Guess a letter!")

    if letter_guess in correct_word:
        print('yes You have guessed correct letter that is present in random choosen word !')
        store_letter += letter_guess
    else:
        print('no!')

    if guess_count == 2:
        print()
        clue_request = input('Would you like to have some Hint(yes or no)?')
        if clue_request.lower().startswith('y'):
            print()
            print('HINT: The first and last letter of the word is: ', clue)
        else:
            print('You\'re Talented!')

print()
print('Now its time to guess. You have guessed', len(store_letter), 'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
if word_guess.lower() == correct_word:
    print('Congrats You have guessed correct word!')
else:
    print('Unlucky! The answer was,', correct_word)

print()
input('Press Enter to leave the program')
