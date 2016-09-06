__author__ = 'technodog'

def poker(hands):
    return max_hand(hands, key=hand_ranks)

def hand_ranks(hand):
    ranks = card_ranks(hand)
    groups = [(ranks.count(i), i) for i in set(ranks)]
    groups.sort(reverse=True)
    card_count, number = zip(*groups)
    staright = (len(card_count) == 5) and (max(number) - min(number) == 4)
    flush = len(set([s for r, s in hand])) == 1
    return (8 if staright and flush else
            7 if card_count == (4, 1) else
            6 if card_count == (3, 2) else
            5 if flush else
            4 if staright else
            3 if card_count == (3, 1, 1) else
            2 if card_count == (2, 2, 1) else
            1 if card_count == (2, 1, 1, 1) else
            0, number)

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def max_hand(iterable, key = None):
    key = key or (lambda x: x)
    return [item for item in iterable if card_ranks(item) == card_ranks(max(iterable, key = key))]