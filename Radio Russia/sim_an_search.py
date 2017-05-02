import random
import dfs
import analyse
import math
import matplotlib.pyplot as plt
import copy

def revert_changes(swapped_state):
    state = swapped_state[0]
    state.signal = swapped_state[1]

def swap_state(map, signals):
    swapped_state = random.choice(map)
    old_signal = swapped_state.signal
    possible_signals = dfs.possible_signals(signals, swapped_state)
    new_signal = random.choice(possible_signals)
    swapped_state.signal = new_signal
    return [swapped_state, old_signal]

def linear_temperature(begin, end, n ,x):
    diff = begin-end
    temperature = begin - (diff * x/n)
    return temperature

def sigmoidal_temperature(begin, end, n, x):
    a = (1/n) * math.log(begin/end)
    temperature = begin * math.exp(-a*x)
    return temperature

def sigmoidal_temperature_2(begin, end, n, x):
    a = (1/(n**2)) * math.log(begin/end)
    temperature = begin * math.exp(-a*(x**2))
    return temperature

def sigmoidal_temperature_3(begin, end, n, x):
    a = (1/(n**3)) * math.log(begin/end)
    temperature = begin * math.exp(-a*(x**3))
    return temperature

def double_sigmoidal_temperature(begin, end, n, x):
    half = float(0.6 * n)
    if x < half:
        a = (1 / (n ** 3)) * math.log(begin / end)
        temperature = begin * math.exp(-a * (x ** 3))
    else:
        i = x - half
        new_begin = begin/3*2
        a = (1 / (half ** 2)) * math.log(new_begin / end)
        temperature = new_begin * math.exp(-a * (i ** 2))
    return temperature

def sinus_sigmoidal_temperature(begin, end, n, x):
    temperature = sigmoidal_temperature_3(begin, end, n, x)
    temperature += begin * 0.05 * math.sin(1/800*x)
    if temperature < 0:
        temperature = end
    return temperature

def sinus_linear_temperature(begin, end, n, x):
    temperature = linear_temperature(begin, end, n, x)
    temperature += begin * 0.05 * math.sin(1/800*x)
    if temperature < 0:
        temperature = end
    return temperature

def sinus_double_sigmoidal_temperature(begin, end, n, x):
    temperature = double_sigmoidal_temperature(begin, end, n, x)
    temperature += begin * 0.05 * math.sin(1/800*x)
    if temperature < 0:
        temperature = end
    return temperature

def sinus_temperature(begin, end, n, x):
    temperature = begin * math.sin((1/n)*math.pi*x) + end
    return temperature

def sinusception_temperature(begin, end, n, x):
    temperature = sinus_temperature(begin, end, n, x)
    temperature += begin * 0.2 * math.sin(1/400 * x)
    temperature += begin * 0.05 * math.sin(1/800 * x)
    if temperature < 0:
        temperature = end
    return temperature

def hill_climber(map, costs, signals, n, begin_temp, end_temp):
    plot = []
    freq = analyse.signal_frequentie(map)
    old_costs = analyse.get_cost(freq, costs)
    lowest_cost = old_costs
    lowest_map = copy.deepcopy(map)
    for x in range(n):
        temperature = sinusception_temperature(begin_temp, end_temp, n, x)
        plot.append(old_costs)
        swapped_state = swap_state(map, signals)
        new_freq = analyse.signal_frequentie(map)
        new_costs = analyse.get_cost(new_freq, costs)
        improvement = old_costs - new_costs
        try:
            chance = math.exp(improvement/temperature)
        except OverflowError:
            chance = 0
        if random.random() < chance:
            old_costs = new_costs
        else:
            revert_changes(swapped_state)
        if old_costs < lowest_cost:
            lowest_cost = old_costs
            lowest_map = copy.deepcopy(map)
    print(temperature)
    print(lowest_cost)
    print(old_costs)
    plt.plot(plot)
    plt.ylabel('costs')
    plt.xlabel('iteraties')
    plt.axis([-100,210000,900,1350])
    plt.show()
    return lowest_map