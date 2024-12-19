import random

import hangman_words as hw
import hangman_art as ha

print(ha.welcome)
print(ha.logo)


for i in ha.stages:
    print(i)


shoosen_word = random.choice(hw.words)