import copy

listX = [[1],[[2]],[3]]
listY = copy.deepcopy(listX)

listY[1][0][0] = 4

print(listX)