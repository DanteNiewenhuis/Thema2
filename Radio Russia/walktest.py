import analyse
import readMap
import sim_an_search
import hill_solve

signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']

with open("randomwalk.txt", 'a') as text:
    for c in range(1,14):
        text.write(str(c) + ',')
        map = readMap.read_complete_map('Russiadfs.txt')
        costs = analyse.get_cost_scheme(c)
        list = hill_solve.random_walker(map, costs, signals, iterations=1000)
        for x in list:
            text.write(str(x) + ',')
        text.write('\n')
