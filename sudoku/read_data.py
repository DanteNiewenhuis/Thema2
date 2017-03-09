def convert(amount, datalist):
    dic = {}
    for conflicts in datalist:
        input = conflicts
        if input in dic.keys():
            x = dic.get(input)
            x += 1
            dic[input] = x
        else:
            dic[input] = 1

    with open('data.txt', 'a') as datafile:
        datafile.write("resultaten met interval van "+ str(amount) + ", groter of gelijk aan ,zonder back.\n\n")
        keylist = list(dic.keys())
        keylist.sort()
        for key in keylist:
            datafile.write(str(key) + ' = ' + str(dic[key]) + '\n')
