#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_unique_list = []
    sum = 0
    for i in my_list:
        if i not in my_unique_list:
            my_unique_list.append(i)
    for j in my_unique_list:
        sum = sum + j
    return (sum)
