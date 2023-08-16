#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        length = 0
        first_char = 'None'
        return (length, first_char)
    return (len(sentence), sentence[0])
