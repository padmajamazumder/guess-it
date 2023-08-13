import random
def hangman():
    word_list = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6
    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'
        print('Guess the word:', guessed_word)
        print('Tries left:', tries)
        guess = input('Enter a letter: ').lower()
        if guess in guessed_letters:
            print('You already guessed that letter.')
            continue
        if guess in word:
            guessed_letters.append(guess)
            if '_' not in guessed_word:
                print('Congratulations! You guessed the word:', word)
                break
        else:
            tries -= 1
            print('Incorrect guess.')
        print('')
    else:
        print('You lost! The word was:', word)
hangman()