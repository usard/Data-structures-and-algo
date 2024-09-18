import random
# word_list = ['anvesh', 'magnus', 'dhoni', 'apple']
word_list = ['apple']
picked_word = random.choice(word_list)
life = 6
game_over = False
match_word = []
for i in range(len(picked_word)):
    match_word.append('_')    
print('welcome to the hangman!')
print('lets start')
while not game_over and life != 0:
    guess_letter = input('enter a guess letter')
    # print('guess_letter :', guess_letter)
    if guess_letter in picked_word :
        for position in range(len(picked_word)):
            if picked_word[position] == guess_letter:
                if match_word[position] == guess_letter:
                    life-=1
                match_word[position] = guess_letter
    else:
        life-=1
    if '_' not in match_word :
        game_over= True
    print(match_word)
if game_over and life != 0 :
   print('you win...')
else:
    print('you lost!')        

