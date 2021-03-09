# it's an example from book but with additional  features
# 1.the program doesn't accept non-alphabetic symbols
# 2.doesn't except more or less than 1 symbol
# 3.some adjustments made (cuz books code sucks a little)
# 4.wrong letters are output so that user could see them constantly
# 5.user can quit if he types 'quit' instead of a letter
# 6.if a word has several similar letters and user picks it
# every instance of this letter is revealed
# 7.it can take a random word from CSV file

import random
allowed_symbols = 'qwertyuiopasdfghjklzxcvbnm'


def hangman(word):
    word = str(word).lower().strip()
    bad_smbl = False

    for i in word:
        if i not in allowed_symbols:
            bad_smbl = True
            break

    if len(word) < 1 or bad_smbl:
        msg = 'A word cannot be empty '
        msg += 'and must contain only alphabet symbols. '
        msg += 'And no spaces are allowed too.'
        msg += 'Your word is: ' + word
        print(msg)
    else:
        stages = [
            '1/8 _______        ',
            '2/8|       |       ',
            '3/8|       |       ',
            '4/8|       0       ',
            '5/8|      /|\      ',
            '6/8|      / \      ',
            '7/8|               ',
            '8/8|HA_HA_UR_DEAD__'
        ]
        mistakes = 0
        wrdlst = list(word)
        board = ["_"] * len(word)
        leave = False
        win = False
        wrng_ltrs = ''
        while mistakes < len(stages):
            char = input('\nenter a letter (or "quit" to exit): ')
            if char.lower() == 'quit':
                leave = True
                print('user left the game')
                break
            if not char in allowed_symbols or len(char) != 1:
                msg = 'you can only enter english letters '
                msg += 'and only one letter per step allowed '
                msg += '(not more or less)'
                print(msg)
                continue
            if char.lower() in wrdlst:
                for num, smbl in enumerate(wrdlst):
                    if smbl == char:
                        board[num] = char
                        wrdlst[num] = '$'
            else:
                mistakes += 1
                if char.upper() not in wrng_ltrs:
                    wrng_ltrs += char.upper() + ' '
            if not '_' in board:
                print('\n You win!!! The word is:')
                print(' '.join(board).upper())
                win = True
                break

            print('\n')
            print(' '.join(board).upper())
            print('Wrong letters: ' + wrng_ltrs)
            print('\n'.join(stages[0:mistakes]))
        if not leave and not win:
            print('\n You lose. Game over. The word was:')
            print(word.upper())

        print('\n'.join(stages[0:mistakes]))


def lst_from_csv(flnm):
    lst = []
    with open(flnm, 'r') as f:
        line = f.readline().strip()
        while line != '':
            lst += line.split(';')
            line = f.readline().strip()
    return lst


def rnd_lst_elt(lst):
    return lst[random.randint(0, len(lst)-1)]


rnd_wrd = ' '
bad_word = True

while bad_word or rnd_wrd == '':
    for i in rnd_wrd:
        if not i.lower() in allowed_symbols:
            rnd_wrd = rnd_lst_elt(lst_from_csv('words.csv'))
            bad_word = True
            break
        else:
            bad_word = False

hangman(rnd_wrd)
