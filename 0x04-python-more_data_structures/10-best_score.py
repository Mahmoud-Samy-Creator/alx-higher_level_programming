#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    else:
        start = 0
        for item in a_dictionary:
            if a_dictionary[item] > start:
                best_score = item
                best = a_dictionary[item]
                start = best
        return best_score
