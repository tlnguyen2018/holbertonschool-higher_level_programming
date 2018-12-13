#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
    else:
        max_sc = max(a_dictionary.keys(), key=(lambda k: a_dictionary[k]))
