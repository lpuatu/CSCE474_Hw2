from scipy.io import arff

data, meta = arff.loadarff('supermarket.arff')
itemSet = [[]]

id = 0
for f in meta:
    itemSet.insert(id, [f, 0])

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 't':
            count = itemSet[j][1]
            itemSet[j][1] = count + 1

for x in itemSet:
    print x
