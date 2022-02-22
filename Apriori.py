from scipy.io import arff
from array import *

#Reads the .arff file
data, meta = arff.loadarff('supermarket.arff')
#Initializes the base itemSet and frequent item set
columns = []
itemSet = []
firstSet = []
freqSet = []
totalCount = 0
#Creates the minimum support and confidence values
minSup = 1000
minConf = 500
#Inserts the base items to the itemsets at value 0
for a in meta:
    itemSet.append([a, 0])
    columns.append(a)
#Iterates through the dataset and counts each occurence of an item, updates the information
for b in range(len(data)):
    for c in range(len(data[b])):
        if data[b][c] == 't':
            count = itemSet[c][1]
            itemSet[c][1] = count + 1
    totalCount = totalCount + 1
#If the items in the set are above the min_sup count then the item is appended to the firstSet
try:
    d = 0
    while d <= len(itemSet):
        if itemSet[d][1] > minSup:
            firstSet.append(itemSet[d])
        d = d + 1
except:
    print ""

#Adds The first set into the freqSet as pairs
for e in firstSet:
    for f in firstSet:
        #Checks if the pair being looked to add already exists or is non entry ie x,x or y,y
        if [f[0],e[0]] not in freqSet and e[0] != f[0]:
            pairSet = [e[0],f[0]]
            h = columns.index(e[0])
            i = columns.index(f[0])
            occurence = 0
            for g in data:
                if g[h] == 't' and g[i] == 't':
                    occurence = occurence + 1
                if occurence > minSup and pairSet not in freqSet:
                    freqSet.append(pairSet)

testCount = 0
for j in freqSet:
    print j
    testCount =  testCount + 1
print testCount
print totalCount
