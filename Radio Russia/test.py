import analyse
import draw
import readMap


map = readMap.read_complete_map('UnitedStatesdfs.txt')

signal_costs = analyse.get_cost_scheme(4)
draw.draw_america_2(map, signal_costs)

