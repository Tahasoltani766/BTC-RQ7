from bip39_list import bip_39
import random
import string

def generate_random_address(random_words):
        prefix = random.choice(["bc1q", "bc1p","3"])
        if prefix == "bc1q":
            initial_suffix = "bc1q"
            possible_characters = string.ascii_lowercase.replace('p', '') + '123456789'
        elif prefix == "bc1p":
            initial_suffix = "bc1p"
            possible_characters = string.ascii_lowercase + '123456789'
        elif prefix == "3":
            initial_suffix = "3"
            possible_characters = string.ascii_lowercase + '123456789'
        else:
            return None
        suffix_length = 59
        suffix = ''.join(random.choice(possible_characters) for _ in range(suffix_length))
        address = initial_suffix + suffix
        print(address, random_words)

def display_random_words(word_list):
    while True:
        if len(word_list) < 12:
            return
        random_words = random.sample(word_list, 12)
        generate_random_address(random_words)


display_random_words(bip_39)




