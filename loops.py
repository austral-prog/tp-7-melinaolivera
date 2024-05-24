def index_of_by_index(word, my_list, start_index):
    if word not in my_list[start_index:]:
        return -1
    
    for i, e in enumerate(my_list[start_index:], start=start_index):
        if word == e:
            return i
    return -1



def index_of_empty(list):
    if not "" in list: return -1
    for i, e in enumerate(list):
        if e == "":
            break
    return i


def index_of(word, my_list):
    if word not in my_list:
        return -1
    for i, e in enumerate(my_list):
        if e == word:
            return i
    return -1

#colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


def put(word, my_list):
    if "" not in my_list:
        return -1
    for i, e in enumerate(my_list):
        if e == "":
            my_list[i] = word
            return i
    return -1
    


def remove(word, my_list):
    if word not in my_list:
        return 0
    count = 0
    for i, e in enumerate(my_list):
        if e == word:
            my_list[i] = ""
            count += 1
    return count
 
