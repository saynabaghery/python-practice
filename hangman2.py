import random
import hangman_art
from hangman_word import word_list
stages=hangman_art.stages
chosen_word=random.choice(word_list)
lives=6
placeholder=""
display=""
print(hangman_art.logo)
print(chosen_word)
for letter in chosen_word:
    placeholder+="_ "
print(placeholder)
correct_letters=[]
while True:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    display=""
    guessl=input("enter your letter ")
    if guessl in correct_letters:
        print(f"you've already guessd letter {guessl}")
    for letter in chosen_word:
        if letter == guessl:
            display += letter
            correct_letters.append(guessl)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("word to guess: "+display)
    if "_" not in display:
        print("****************************YOU WIN****************************")
        break
    if guessl not in chosen_word:
        lives-=1
        print(f"you guessed {guessl}, that's not in the word. you lose a life")
        print(stages[lives])
        if lives==0:
            print(f"IT WAS {chosen_word}!")
            print(f"***********************YOU LOSE**********************")
            break




