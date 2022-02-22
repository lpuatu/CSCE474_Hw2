from scipy.io import arff
from array import *

#Reads the .arff file
data, meta = arff.loadarff('supermarket.arff')
#Initializes the base itemSet and frequent item set
itemSet = []
firstSet = []
freqSet = []
#Creates the minimum support and confidence values
minSup = 300
minConf = 500
#Inserts the base items to the itemsets at value 0
id = 0
for f in meta:
        itemSet.insert(id, [f, 0])
        id = id + 1
#Iterates through the dataset and counts each occurence of an item, updates the information
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 't':
            count = itemSet[j][1]
            itemSet[j][1] = count + 1
#If the items in the set are above the min_sup count then the item is appended to the firstSet
try:
    p = 0
    while p <= len(itemSet):
        if itemSet[p][1] > minSup:
            firstSet.append(itemSet[p])
        p = p + 1
except:
    print ""
#Adds The first set into the freqSet as pairs
try:
    for b in firstSet:
        w = 1
        while w <= len(firstSet):
            if [b,firstSet[w]] not in freqSet:
                pairSet = [b,firstSet[w]]
                freqSet.append(pairSet)
                w = w + 1
except:
    print ""

for y in freqSet:
    print y
