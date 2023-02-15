import string
import random
words = ["pes","slon","kocka","krava","morce","tygr","lev","husa","zirafa","ptak","mys"]

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #mnozina pismena ktera se nachazi v tom slove
    alphabet =  set(string.ascii_uppercase)
    used_letters = set()

    lives= 8
    while lives >0 and len(word_letters) > 0:
        print("Ahoj! Vítej v hádance zvířat, požívej prosím písmena bez háčků a čárek, ty máš",lives,"životů a zatím jsi použil tyto písmena")
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append("-")
        print("součastné slovo je: "," ".join(word_list))

        user_letter = input("zadejte písmeno:").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add((user_letter))
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")
            else:
                lives = lives - 1
                print("tvoje písmeno:",user_letter,"se nenachází v daném slově.")
        elif user_letter in used_letters:
            print("toto písmeno jsi uz použil.")
        else:
            print("Nezadal jsi písmeno.")
    if lives == 0:
        print("Prohrál jsi, došli ti životy.")
    else:
        print("Vyhrál jsi, hádané slovo bylo", word,"!!!")


hangman()