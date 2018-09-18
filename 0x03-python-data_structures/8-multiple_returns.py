#!/usr/bin/python3
def multiple_returns(sentence):
    s_len = len(sentence)
    if s_len > 0:
        return s_len, sentence[0]
    else:
        return s_len, None
