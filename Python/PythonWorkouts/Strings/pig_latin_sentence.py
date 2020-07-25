#!/usr/bin/env python

def pig_latin_sentence(sentence):
    result = []
    for word in sentence.split():
        
        if word[0] in 'aeiou':
            result.append(f'{get_word}way')
        else:
            remain_letter = word[1::]
            result.append(f'{remain_letter}{get_word[0]}ay')
    return '.'.join(result)

print(pig_latin_sentence("this is a test"))
        