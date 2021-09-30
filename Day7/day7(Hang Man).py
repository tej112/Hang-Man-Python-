import random
from art import *
from words import *

#words that are guessed
# word_list = ["aardvark", "baboon", "camel"]
lives = len(stages)-1
print(logo)
#gets a random word from the list of words and prints if you want
selected = word_list[random.randint(0,len(word_list)-1)]
print(f"the selected word is {selected}")

#generates a list of '_' size of random word selected
blank = ['_' for i in range(len(selected))]
win = False
fig = -1
guessed = []

# runs while game is not over i.e., if player won or lost
while not win:
    #Checks if there are any '_' in guessing
    if '_'not in blank:
        print("You Win")
        win = True
        break
    
    #takes input from user
    letter = input("guess a letter: ").lower()
    
    if letter in guessed:
        print("letter already used try with different letter ")
    if letter not in guessed:
        guessed.append(letter)
    print(f"\nguessed letters are: -> {' '.join(guessed)}")
    #check if the user input is in selected word
    if letter not in selected:
        #if lives exhaust prints that user lost and breaks the loop and exits
        if lives == 0:
            win = True
            print("You lose")
            break
        lives -= 1
        fig -= 1
        print(stages[fig])
        print("The word is :")
        print(' '.join(blank))
        print('\n')
        if fig == -7:
            print("You lose!!!")
            print(f"The word is {selected}")
            break
    else:
        #if user input is in randoml selected word then it replaces '_' s with guessed word and prints
        for i in range(len(selected)):
            if letter == selected[i]:
                blank[i] = letter
        print("The word is :")
        print(' '.join(blank))
        print('\n')
    
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

