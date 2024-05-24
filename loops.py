def index_of_by_index(word, list, index):
    if not word in list[index:]: return -1
    
    for i, e in enumerate(list[index:]):
        if word == e:
            return i + len(list[:index])


def index_of_empty(list):
    if not "" in list: return -1
    for i, e in enumerate(list):
        if e == "":
            break
    return i

        



def index_of(word, list):
    
    if not word in list: return -1
    for i, e in enumerate(list):
        if e == word:
            break
    return i
    

#colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
def put(word, list):
    if not "" in list: return -1 #si no hay un "" en la list directo que ponga -1
    for i, e in enumerate(list): # i = index de la palabra buscada, e = elemento ubicado en ese index
        if e == "": # defino para que frene en el momento en el que encuentre un "" y ahi hace o de abajo
            break
    list[i] = word #reemplazo en el index que esta el ""(vacio) por la word
    return i #returnea la index
    


def remove(word, list):
    if not word in list: return 0 # si la word no esta en list directo te pone 0
    count = 0 # cantidad de words que hay
    for i, e in enumerate(list): 
        if e == word:
            list[i], count = "", count +1 # En la posicion i, se reemplaza por count = "" y al pasar 1 vez se suma uno, 
                                          # y al pasar otra vez se cambia denuevo por la posicion de la otra palabra y 
                                          # se le suma 1 mas a su count, osea va a decir 2
    return count
