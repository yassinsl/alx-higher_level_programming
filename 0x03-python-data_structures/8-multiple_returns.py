#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    else :
        lenght = len(sentence)
        first = sentence[0]
        return lenght, first
