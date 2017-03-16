import readMap
import analyse

map = readMap.readStates('UnitedStates.txt')
print(analyse.analyse_adjacent_states(map))