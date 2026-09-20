import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
lives=6
placeholder=""
display=""
print(chosen_word)
for letter in chosen_word:
    placeholder+="_ "
print(placeholder)
correct_letters=[]
while True:
    display=""
    guessl=input("enter your letter ")
    for letter in chosen_word:
        if letter == guessl:
            display += letter
            correct_letters.append(guessl)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if "_" not in display:
        print("You win.")
        break
    if guessl not in chosen_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("you lost.")
            break




