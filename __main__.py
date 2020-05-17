
import string
import random
from func import read_letters, open_dictionary, checkingwords, check_panagram, calc_score, printList

def main():
    points = 0
    user_words = []
    user_words_set = set()
    user_choice = True
    dict_set = open_dictionary("/Users/nupurdave/Desktop/Misc/Anagrams-project/test_atom/words.txt")
    print("Would you like to choose your letters or have random ones?")
    print("1. Random [HARD]  2. Choose [EASY]")
    randinput = input("Please enter 1 or 2: ")
    if(randinput == "1"):
        vowel_string = "aeiou"
        random_vowel_1 = random.choice(vowel_string)
        random_vowel_2 = random.choice(vowel_string)
        if(random_vowel_1 == random_vowel_2):
            random_vowel_2 = random.choice(vowel_string)
        vowel_set = set()
        vowel_set.add(random_vowel_1)
        vowel_set.add(random_vowel_2)
        letterset = set()
        lower_upper_alphabet = string.ascii_lowercase
        for i in range(0,4):
            tempbool = True
            while(tempbool):
                random_letter = random.choice(lower_upper_alphabet)
                if(random_letter not in letterset):
                    letterset.add(random_letter)
                    tempbool = False
                elif(random_letter in letterset):
                    tempbool = True
        letterset = letterset|vowel_set
        specialletter_temp = random.sample(letterset,1)
        specialletter = ''.join(specialletter_temp)
        print("Your letters are: ")
        for l in letterset:
            print(l, end=" ")
        print()
        print("Your special letter is " + str(specialletter))
    elif(randinput == "2"):
        print('Which letters do you want to make an anagram with?')
        stringWords = input('Please enter 6 and seperate with commas:')
        #specialletter = ""
        specialletter = input('What is the special letter?')
        specialletter = char(specialletter)
        letterset = set()
        letterset = read_letters(stringWords, letterset)
    while(user_choice):
        special_letter_not_used = True
        user_guess = input('Enter a word (type *done* if you are done):')
        print("-------------------------------")
        word_split = list(user_guess)
        boolean = True
        if(user_guess == "*done*"):
            user_choice = False
            print("End of game")
            print("You got " + str(points) + " points!!")
            printList(user_words)
            break
        elif(user_guess in user_words_set):
            print('Already have that word')
            continue
        for letter in word_split:
            if(letter in letterset):
                if(letter == specialletter):
                    special_letter_not_used = False
            else:
                boolean = False
                print('Uses unassigned letters')
                break
        if(special_letter_not_used):
                print('You didnt use the special letter!')
        elif(boolean):
            word = checkingwords(user_guess, dict_set, user_words)
            if (word == ""):
                print("That is not a word in the dictionary")
            else:
                user_words.append(word)
                points = points + check_panagram(word_split, letterset)
                points = points + calc_score(len(word_split))
                temp = calc_score(len(word_split)) + check_panagram(word_split, letterset)
                print("You won " + str(temp) + " points!!")
        for item in user_words:
            user_words_set.add(item)
        printList(user_words)
        print('Points: ' + str(points))

if __name__ == '__main__':
    main()
