TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# DO NOT MODIFY THE initialize function
def initialize(word_list):
    """
    Takes a list of words as a parameter.
    Starting with the word in the word_list,
    starts a new game using the word.
    If the user wants to play again, starts the next
    game with the next word.
    Runs until user doesn't want to play or
    until it runs out of new words.
    """
    i = 0
    while i < len(word_list) and start_new_game(word_list[i], TRIES):
        i += 1


def obfuscate(word, letters_guessed):
    """
    Takes the current word being guessed and
    a string containing letters that user has
    tried to guess during current playthrough.
    Returns a string, that only shows letters
    that the user has guessed correctly. Return
    the guessed letter in uppercase. The letters,
    that user still has to guess are replaced with
    underscores.
    Example:
        input: 'claire','abcd'
        ouput: 'C_A___'
    Example:
        input: 'Amanda','etai'
        output: 'A_A__A'
    Example:
        input: 'Obi-Wan KENOBI','oteai'
        output: 'O_I-_A_ _E_O_I'
    """
    ret_val = ''
    for character in word:
        if ALPHABET.find(character) == -1:
            ret_val += character
            continue
        addtoretval = '_'
        for letter in letters_guessed:
            if letter == character:
                addtoretval = letter
                break
        ret_val += addtoretval

    return ret_val


def start_new_game(word, max_tries):
    """
    # Arguments
    Takes a word (string) that the user has to guess,
    and max_tries (int) - the number of tries user has
    before he loses the game.
    # Description
    Before prompting the user always show the letters he still hasn't tried to guess.
    This function should prompt user for a letter, and
    check, whether the letter guessed is in the word.
    If user guessed correctly, reveal the letter to him.
    If user guessed wrong, decrease the number of tries and show the amount of tries remaining.
    Keep asking user for more letters, until he wins or loses.
    When the game ends, ask user to choose, whether they want
    to play the game again.
    If the user types 'n', return False.
    If the user types 'y', return True.
    User will only input 'n','N','y' or 'Y', so no need to handle other cases
    # Return
    Returns a boolean, stating whether user
    wants to have another game.
    Example:
        input: 'Obi-Wan Kenobi',
        execution: user wins, wants to play again,
                    types 'y' when prompted
        output: True
    Example:
        input: 'GANDALF',
        execution: user wins, doesn't want to play again,
                    types 'n' when prompted
        output: False
    """

    guessed_letters = ''
    nonguessed_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word = word.upper()
    print REMAINING_TRIES + str(max_tries)
    print obfuscate(word, '')

    while max_tries > 0 and obfuscate(word, guessed_letters) != word:
        print LETTERS_LEFT
        print nonguessed_letters
        print INPUT_PROMPT

        validinputentered = False
        while not validinputentered:
            character = raw_input()
            if len(character) > 1 or len(character) == 0 or ALPHABET.find(character.upper()) == -1:
                print INVALID_INPUT
                continue

            max_tries -= 1
            nonguessed_letters = nonguessed_letters.replace(character.upper(), '')
            guessed_letters = guessed_letters + character.upper() if guessed_letters.find(character.upper()) == -1 else guessed_letters
            print REMAINING_TRIES + str(max_tries)
            print obfuscate(word, guessed_letters)
            validinputentered = True

    if obfuscate(word, guessed_letters) == word:
        print GAME_WON_PHRASE
    else:
        print GAME_LOST_PHRASE

    print OFFER_NEXT_GAME
    playerwantstocontinue = raw_input()

    if playerwantstocontinue.upper() == 'Y':
        return True
    elif playerwantstocontinue.upper() == 'N':
        return False


initialize(['Obi-Wan Kenobi', 'Alladin'])
