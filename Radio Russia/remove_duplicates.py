import analyse

no_dups_maps = []
with open("randommaps.txt", "r") as maps:
    for line in maps:
        split_line = line.split(',')[:-1]
        if split_line not in no_dups_maps:
            no_dups_maps.append(split_line)

signal_costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}

plot = []
dic = {}
for state in no_dups_maps:
    costs = 0
    for signal in state:
        costs += signal_costs[signal]
    plot.append(costs)
    if costs in dic:
        x = dic[costs]
        dic[costs] = x + 1
    else:
        dic[costs] = 1
print(dic)
analyse.bar_plot(dic)
