#!/user/bin/python3
def multiple_returns(sentence):
    tuple_a = (len(sentence), sentence[:1])
    if (len(sentence) == 0):
        sentence[0] = None
        return (tuple_a)
