__author__ = 'technodog'

def is_pangram(sentence):
    alphabetSet = set('abcdefghijklmnopqrstuvwxyz')
    sentenceSet = set(sentence.lower())
    return sentenceSet.issuperset(alphabetSet)