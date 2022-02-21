from scipy.io import arff
from array import *

data, meta = arff.loadarff('supermarket.arff')
itemSet = [[]]

id = 0
for f in meta:
    itemSet.insert(id, [f, 0])
    id = id + 1

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 't':
            count = itemSet[j][1]
            itemSet[j][1] = count + 1

for x in itemSet:
    print x
