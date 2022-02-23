from scipy.io import arff
from array import *

#Reads the .arff file
#fileName = input('Enter file name: ')
data, meta = arff.loadarff('supermarket.arff')
#Initializes the base itemSet and frequent item set
columns = []
itemSet = []
firstSet = []
freqSet = []
previousfreqSet = []
totalCount = 0
#Creates the minimum support and confidence values
minSup = input('Enter minimum support: ')
minConf = 500
dataTrue = 't'
#Inserts the base items to the itemsets at value 0
for a in meta:
    itemSet.append([a, 0])
    columns.append(a)
#Iterates through the dataset and counts each occurence of an item, updates the information
for b in range(len(data)):
    for c in range(len(data[b])):
        if data[b][c] == dataTrue:
            count = itemSet[c][1]
            itemSet[c][1] = count + 1
    totalCount = totalCount + 1
#If the items in the set are above the min_sup count then the item is appended to the firstSet

for d in itemSet:
    if d[1] > minSup:
        firstSet.append(d[0])

#Adds The first set into the freqSet as pairs
for e in firstSet:
    for f in firstSet:
        #Checks if the pair being looked to add already exists or is non entry ie x,x or y,y
        if [f,e] not in freqSet and e != f:
            pairSet = [e,f]
            occurence = 0
            for g in data:
                if g[columns.index(e)] == dataTrue and g[columns.index(f)] == dataTrue:
                    occurence = occurence + 1
                if occurence > minSup and pairSet not in freqSet:
                    freqSet.append(pairSet)
                    previousfreqSet.append(pairSet)
                    break

boolean = True
while boolean:
    boolean = False
    addedSet = []
    for k in previousfreqSet:
        for l in firstSet:
            newSet = list(k)
            if l not in newSet:
                newSet.append(l)
                newCount = 0
                for n in data:
                    for m in newSet:
                        if n[columns.index(m)] == dataTrue:
                            verify = True
                        else:
                            verify = False
                            break
                    if verify:
                        newCount = newCount + 1
                if newCount >= minSup:
                    freqSet.append(newSet)
                    addedSet.append(newSet)
                    boolean = True
    previousfreqSet = []
    previousfreqSet = addedSet

sortedFreq = [frozenset(o) for o in freqSet]
cleanFreq = set(sortedFreq)

testCount = 0
for j in cleanFreq:
    print list(j)
    testCount =  testCount + 1
print testCount
