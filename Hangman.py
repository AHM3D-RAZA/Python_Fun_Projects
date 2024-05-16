import random

WORDS = ['hangman', 'apple', 'potato', 'cool', 'polo', 'chill', 'break', 'bad', 'look', 'bandage', 'snake', 'yakuza']

answer = random.choice(WORDS)
answer_tokens = list(answer)
dashes = ''
print(answer)
print(len(answer_tokens) * '_')
word = ''
wrongs = 0
HANGED = False

while word != answer:
    guess = input('Enter your guess: ')
    if guess == answer_tokens[0]:
        answer_tokens.remove(guess)
        word += guess
    else:
        wrongs += 1
        if wrongs >= 8:
            print('***YOU LOST AND WERE HANGED!***\n  |\n Q|\n/|\\\n/ \\')
    print(word + len(answer_tokens)*'_')


print('**CONGRATS! YOU WON!')