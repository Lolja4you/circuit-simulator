dictionary = {1: [4], 2: [1, 3], 3: [4], 5:[4]}


loop = []
for key, item in dictionary.items():
    if not key  in loop: loop.append(key)

    for i in item:
        if not i in loop: loop.append(i)

