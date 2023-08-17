#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    else:
        start = 0
        for item in a_dictionary:
            if a_dictionary[item] > start:
                best = a_dictionary[item]
                start = best
        return best
