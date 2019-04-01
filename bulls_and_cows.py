import random


def generate_cipher():
    return random.sample(range(10), 4)


def get_bulls_and_cows(cipher, guess):
    assert len(cipher) == len(guess) == 4, 'cipher and guess must be lists of length 4'
    bulls = 0
    cows = 0
    for i in range(len(cipher)):
        if guess[i] == cipher[i]:
            bulls += 1
        else:
            cows += 1

    return bulls, cows


def play_game():
    # this function should use both generate_cipher and get_bulls_and_cows
    # inside and provide a command-line interface to play the game
    # while keeping the results of previous attempts as described in the pdf
    # there should be some basic validation of the user input
    # (that its a number of 4 unique digits)

    # here's an example of the game played with the cipher being [1, 3, 9, 7]
    # feel free to remove when you understood it if it feels too cumbersome :)
    # you can also play it here: http://www.mathsisfun.com/games/bulls-and-cows.html
    # pick the 0-9, 4 codes option

    # Enter your guess without spaces:
    # 1234
    # 1234 bulls: 1, cows: 1

    # Enter your guess without spaces:
    # 3945
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2

    # Enter your guess without spaces:
    # 1398
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0

    # Enter your guess without spaces:
    # 1298
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0

    # Enter your guess without spaces:
    # 1397
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0
    # 1397 bulls: 4, cows: 0

    # Congrats, You win
    game_running = True
    cipher = generate_cipher()
    while game_running:
        user_input = raw_input('Enter your guess without spaces:')

        if not user_input.isdigit():
            continue

        result = get_bulls_and_cows(cipher, list(map(int, list(user_input))))
        if result == (4, 0):
            game_running = False
        else:
            print(user_input + ' bulls: ' + str(result[0]) + ', cows: ' + str(result[1]))
    print('Congrats, You win')

play_game()
#print get_bulls_and_cows([1,2,3,4],[1,2,3,4])# -> (4, 0)
#print get_bulls_and_cows([1,2,3,4],[2,1,4,3])# -> (0, 4)
#print get_bulls_and_cows([1,2,3,4],[1,6,2,3])# -> (1, 2)
#print get_bulls_and_cows([1,2,3,4],[5,6,7,8])# -> (0, 0)