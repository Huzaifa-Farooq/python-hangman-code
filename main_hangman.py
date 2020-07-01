import random
import time

with open('words.txt') as f:
    words = list(f)

word = random.choice(words)
clue_limit = 5
clue_given = 0
attempts = 0

def give_clue(word):
    word = list(word)
    hint = random.choice(word)
    return hint

print("\t\t## Welcome to the game of HANGMAN ##")
time.sleep(0.6)

print("\t\t You can guess wrong 8 times")

time.sleep(0.6)
print(f"The given word is {len(word)} letters long. Fill in those blanks")

word_guess = []
for i in range(len(word) - 1):
    word_guess.append('*')


status = input("\nDo you want to start with a little clue(Y/N): ").upper()

if status == 'Y' and clue_given < clue_limit:
    clue = give_clue(word)
    print(f"There you go {clue}")
    clue_given += 1
    print(f"Hints remaining: {clue_limit - clue_given}")

elif status == 'N' :
    print("Alright..")

word_list = list(word)
del word_list[-1]

response_list = []
registered_response = []

print("REMEMBER!  The given word does not include special letters or numbers.\n")

game_status = 'Y'
while game_status == 'Y':

    while len(response_list) <= len(word_list):

        if attempts < attempts_lim:
            response=input(f"Make your guess: ").upper()

            if response not in registered_response:

                if response in word_list:
                    print("That was Correct!")
                    for i in range(len(word_list)):
                        if word_list[i] == response:
                            response_list.insert(i, response)
                            del word_guess[i]
                            word_guess.insert(i, response)
                    print(f"\nYour progress so far: ")
                    print(word_guess)

                if response not in word:
                    print("\nSorry. That was Incorrect!\n You lost ont attempt")
                    attempts += 1
                    print(f"Remaining Attempts: {attempts_lim - attempts}")

            if response_list == word_list:
                break

        elif attempts >= attempts_lim:
            break

    if response_list == word_list:
        print("Congratulations You've guessed the Word..")

    else:
        print(f"\nYou've lost the game.\nThe word was {word}")

    game_status = input("\n\nWant to play again?(Y/N): ").upper()
