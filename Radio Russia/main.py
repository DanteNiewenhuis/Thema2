import readMap
import dfs
import analyse
import hill_solve
import sim_an_search
import draw

scheme = analyse.get_cost_scheme(1)
draw.bar_plot(scheme,'Signal', 'Costs', 'Cost per signal')