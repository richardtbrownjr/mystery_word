import random
import os

def check_word_length(word_length):
    #based on word_length pull those words from the larger dict pass to word_choice
    if word_length == 'e':
        level_of_word = '1'
    elif word_length == 'n':
        level_of_word = '2'
    else:
        level_of_word = '3'
    return word_choice_from_dict(level_of_word)

def word_choice_from_dict(level_of_word):
    #based on choice create a dictionary
    words = []
    with open('/usr/share/dict/words','r') as f:
        for line in f:
            line = line.rstrip()
            if level_of_word =='1':
                if len(line) >= 4 and len(line) <= 6:
                    words.append(line)
            if level_of_word =='2':
                if len(line) >= 7 and len(line) <=9:
                    words.append(line)
            if level_of_word =='3':
                if len(line) >= 8:
                    words.append(line)
    return words

def draw(hangman_word, word_character_length, guesses):
    spacing_the_guess = []
    os.system('clear')
    print("                       Play Hangman  ")
    print('***********************************************')
    print('  Do you want (E)asy (N)ormal or (H)ard mode: ')
    print('')
    print(hangman_word, 'Tis the word')
    holder_hangman_word = list(hangman_word)
    for i, letter in enumerate(holder_hangman_word):
        spacing_the_guess.append('__  ')
        if letter in guesses:
            spacing_the_guess[i] = letter.upper()
        print(spacing_the_guess[i], end=' ')
    return ' '.join(spacing_the_guess)

def get_bad_guesses_count(hangman_word, guesses):
    count = 0
    for guess in guesses:
        if guess not in hangman_word:
            count += 1
    return count

def has_more_guesses(hangman_word, guesses):
    return get_bad_guesses_count(hangman_word, guesses) < 2

def checking_if_letter_is_correct(hangman_word, word_character_length):
    guesses = []

    while has_more_guesses(hangman_word, guesses):
        print('')
        try:
            guess_letter = str(input("\nGuess one letter in the hangman secret word ")).lower()
        except:
            print("That is not valid input. Please try again.")
            continue
        else:
            if not guess_letter.isalpha():
                print("That's not a letter. Please try again.")
                continue
            elif len(guess_letter) > 1:
                print("That's more than one letter. Please try again.")
                continue
            elif guess_letter in guesses:
                print("You have already guessed that letter. Please try again.")
                continue
            else:
                pass

        guesses.append(guess_letter)
        draw(hangman_word, word_character_length, guesses)
        count = get_bad_guesses_count(hangman_word, guesses)
        print('test 2')
        if count >=1:
            print('')
            print('You have {} guesses left.'.format(8 - count))
            #print('Wow you have won!')
            
            print('wow')
def play_again():
    play_again = input(' Do you want to try again (Y)es or (N): ').lower()
    if play_again == 'y':
        main()
    else:
        print('Thanks for trying.  See you soon!')

def easy_words(word_list):
    words = []
    with open('/usr/share/dict/words','r') as f:
        for line in word_list:
            if len(line) >= 4 and len(line) <= 6:
                words.append(line)
    return words

def medium_words(word_list):
    words = []
    with open('/usr/share/dict/words','r') as f:
        for line in word_list:
            if len(line) >= 6 and len(line) <= 8:
                words.append(line)
    return words

def hard_words(word_list):
    words = []
    with open('/usr/share/dict/words','r') as f:
        for line in word_list:
            if len(line) >= 8:
                words.append(line)
    return words

def random_word(word_list):
    randwords = []
    word = random.choice(word_list)
    randwords.append(word)

    return word

def display_word(hangman_word, word):
        spacing_the_guess = []
        for letter in hangman_word:
            spacing_the_guess.append('_')
        for i, letter in enumerate(list(hangman_word)):
            if letter in word:
                spacing_the_guess[i] = letter.upper()
        return ' '.join(spacing_the_guess)

def is_word_complete(hangman_word, guesses):
    for i in hangman_word:
        if i not in guesses:
            return False
    return word

def main():
    os.system('clear')
    print("                       Play Hangman  ")
    print('***********************************************')
    word_length = input(' Do you want (E)asy (N)ormal or (H)ard mode: ').lower()
    words = check_word_length(word_length)

    hangman_word = random_word(words)
    print(hangman_word, 'Tis the word')
    word_character_length=len(hangman_word)
    print("This secret word is {} characters long. Good luck".format(word_character_length))
    print('')
    print('')
    print('__ '*word_character_length)

    checking_if_letter_is_correct(hangman_word, word_character_length)

    #is_word_complete(hangman_word, guesses)

    play_again()

if __name__ == '__main__':
    main()
