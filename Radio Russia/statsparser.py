mem = {}

with open("sinsigmoid.txt", 'r') as stats:
    for line in stats:
        split_line = line.split(',')
        list = []
        for x in split_line[1:]:
            if x is not '\n' or None:
                list.append(int(x))
        mem[split_line[0]] = list

with open("sinccalc.txt", 'w') as text:
    for key in mem:
        text.write(str(key) + ': ')
        text.write('avg: ')
        avg = sum(mem[key])/len(mem[key])
        text.write(str(avg))
        text.write(' - ')
        lowest = mem[key][0]
        highest = mem[key][0]
        for x in mem[key]:
            if x < lowest:
                lowest = x
            if x > highest:
                highest = x
        text.write('low: ' + str(lowest) + ' - high: ' + str(highest))
        text.write('\n')

