#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        firstchar = None
    if len(sentence) > 0:
        firstchar = sentence[0]
    return (length, firstchar)
