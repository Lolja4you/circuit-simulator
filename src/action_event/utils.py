def get_last_pk(dictionary):
    pk_list = list(dictionary.keys())
    if len(pk_list) == 0:
        last_pk = 0
    else:
        last_pk = pk_list[-1]

    return int(last_pk)


def get_last_pk_components(circuit):
    try:...
        #last_pk = keys()[-1]
    except:...
        #last_pk = 1
    #return last_pk


def serializer(dictionary) -> str:
    string = []
    for key, items in dictionary.items():
        string.append(f'{key} : {items}\n')

    return string