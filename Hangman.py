import random
import string
print("Welcome to Hangman")
print("You have 8 errors before the game ends")

with open("words.txt") as words_file:
    words = words_file.read().splitlines()
    chosen_word = random.choice(words).strip()

check_answer = chosen_word[:] 
answer = len(check_answer)*"_" 
wrong_count = 0
entered_letters = ""

while wrong_count != 8:
    print("Your word is " + answer)
    user_answer = input("What letter would you like to guess? ")
    
    while user_answer in entered_letters:
        user_answer = input("Oops, You have already guessed this letter! Input a different letter: ")
        
    while len(user_answer) != 1 and user_answer not in string.ascii_letters.lower():
        user_answer = input("Please input a single letter: ") 
        
    if user_answer not in check_answer.lower():
        wrong_count += 1
        print("Sorry, your guess is not in the word. You have " + str(8 - wrong_count) + " more guesses.")
        
    while user_answer in check_answer.lower():
        index = check_answer.lower().find(user_answer)
        if index == 0:
            answer = answer[0:index] + user_answer.upper() + answer[index + 1:]
        else:
            answer = answer[0:index] + user_answer + answer[index + 1:]
        check_answer = check_answer[0:index] + "_" + check_answer[index + 1:]
        
    entered_letters += user_answer
    
    if answer == chosen_word:
        print("CONGRATULATIONS! You guessed the mystery word: " + chosen_word")
        print(check_answer)
        break

if wrong_count == 8:
    print(f"Sorry, the correct answer is {chosen_word}")
    
