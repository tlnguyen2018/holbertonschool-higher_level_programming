def search_replace(my_list, search, replace):
    return ([i if i is not search else replace for i in my_list])
