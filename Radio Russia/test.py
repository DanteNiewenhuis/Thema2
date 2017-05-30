import analyse
<<<<<<< HEAD

for x in range(1, 19):
    scheme = analyse.get_cost_scheme(x)
    with open('scheme.txt', 'a') as text:
        text.write(str(scheme['zA']))
        text.write(',')
        text.write(str(scheme['zB']))
        text.write(',')
        text.write(str(scheme['zC']))
        text.write(',')
        text.write(str(scheme['zD']))
        text.write(',')
        text.write(str(scheme['zE']))
        text.write(',')
        text.write(str(scheme['zF']))
        text.write(',')
        text.write(str(scheme['zG']))
        text.write(',')
        text.write('\n')
=======
import draw
import readMap


map = readMap.read_complete_map('UnitedStatesdfs.txt')

signal_costs = analyse.get_cost_scheme(4)
draw.draw_america_2(map, signal_costs)

>>>>>>> origin/master
