def index_of_by_index(string, lst, start_index):
    try:
        return lst.index(string, start_index)
    except ValueError:
        return -1
def index_of_empty(lst):
    try:
        return lst.index(" ")
    except ValueError:
        return -1
def index_of(string, lst):
    try:
        return lst.index(string)
    except ValueError:
        return -1

def put(string, lst):
    index = index_of_empty(lst)
    if index != -1:
        lst[index] = string
    return index

def remove(string, lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == string:
            lst[i]=" "
            count += 1
        return count

colors = ["Red", "Green", "White", "Black", "Pink","Yellow","Black"]
print(index_of("Black", colors))
print(index_of("Blue", colors))
print(index_of_by_index("Black", colors,1))
print(index_of_by_index("Black", colors,4))
print(index_of_by_index("Green", colors,2))
colors1 = ["Red", "Green", " ", " ", "Pink"," ","Black"]
colors2 = ["Red", "Green", "White", "Black", "Pink","Yellow","Black"]
print(index_of_empty(colors1))
print(index_of_empty(colors2))
print(put("Blue", colors1))
print(remove("Black", colors))
print(remove("Blue", colors))
