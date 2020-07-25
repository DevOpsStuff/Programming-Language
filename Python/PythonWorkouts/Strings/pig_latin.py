#!/usr/bin/env python3

def pig_latin(get_word):
    
    if get_word[0] in 'aeiou':
        return f'{get_word}way'
    else:
        remain_letter = get_word[1::]
        return f'{remain_letter}{get_word[0]}ay'

print(pig_latin('prasanna'))