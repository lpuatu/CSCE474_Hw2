from scipy.io import arff

data, meta = arff.loadarff('supermarket.arff')
itemSet = [[]]


for i in range(columns):
    for j in range(row):
        if(j == 't'):
            count = count + 1

print count

for k in data:

    sum(x.count('t') for x in i)
