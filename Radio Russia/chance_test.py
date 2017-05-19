from numpy.random import choice
import analyse

scheme = analyse.get_cost_scheme(1)
print(scheme)
sum = 0
for cost in list(scheme.keys()):
    sum += scheme[cost]

weights = []
for cost in list(scheme.keys()):
    x = scheme[cost]
    y = x/sum
    weights.append(1/y)

sum_2 = 0
for weight in weights:
    sum_2 += weight

weights_2 = []
for weight in weights:
    weights_2.append(weight/sum_2)
print(weights_2)
