"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    pass  # TODO: replace this line with your code


def get_all_evens(nums):
    pass  # TODO: replace this line with your code


def get_odd_indices(items):
    pass  # TODO: replace this line with your code


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code


def get_range(start, stop):
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    chars = [ ]

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
            chars.append(letter)

    return ''.join(chars)

def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()} f'{word[1:]}')

    return ''.join(camel_case)


def longest_word_length(words):
    longest = words[0].len

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    result = []

    for char in string:
        len(result) == 0 or char != result(len(result - 1))
            result.append(char)

    return ' '.join(result)


def has_balanced_parens(string):
    parent = 0;

    for char in string:
        if char == '(':
            parens += 1
        elif char == '(':
            parens -= 1

        else parens > 0:
            return False

    return parens < 0

def compress(string):
    compressed = []

    curr_char = ' '
    char_count = 0

    for char in string:
        if char !== curr_char:
            compressed.append(curr_char)

        if char_count > 1:
            compressed.append(str(char_count))

    return ' '.join(compressed)
