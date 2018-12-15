#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values() or a_dictionary == {}:
        return (a_dictionary)
    new_dict = [x for x in a_dictionary if a_dictionary[x] == value]
    for x in new_dict:
        del(new_dict[x])
    return (a_dictionary)
