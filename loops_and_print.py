def enumerate_list(list):

    lists = []
    lists2 = []
    for e in list:
        if e != "":
            lists.append(e)
    for i, e in enumerate(lists[0:]):
        lists2.append(f"{i}. {e}")
    return lists2

#retorna la lista:
# ["0. Red", "1. Green", "2. White", "3. Black"]
def enumerate_backwards(list):
    lists = []
    lists2 = []
    for e in list:
        if e != "":
            lists.append(e[::-1])
    for i, e in enumerate(lists[0:]):
        lists2.append(f"{i}. {e}")
    return lists2
