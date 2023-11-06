#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        tuple_a = (0, None)
    else:
        tuple_a = (len(sentence), sentence[:1])
    return (tuple_a)
