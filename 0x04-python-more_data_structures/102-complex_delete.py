#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary or a_dictionary == {}:
        return (a_dictionary)
    new_dic = [x for x in a_dictionary if a_dictionary[x] == value]
    for x in new_dic:
        del new_dic(x)
    return (new_dic)
