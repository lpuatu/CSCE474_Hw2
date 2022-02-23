from scipy.io import arff
from array import *
import timeit

timer = timeit.default_timer()

#Reads the .arff file
file = input('Enter file name(include ' '): ')
data, meta = arff.loadarff(file)
#Initializes the base itemSet and frequent item set
columns = []
itemSet = []
firstSet = []
freqSet = []
supportSet = []
previousfreqSet = []
totalCount = 0
#Creates the minimum support and confidence values
minSup = input('Enter minimum support: ')
minConf = input('Enter minimum confidence: ')
dataTrue = input('Enter the value in the set when the data is true(include ' '): ')
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
    if float(d[1])/float(totalCount)>= float(minSup):
        firstSet.append(d[0])
        supportSet.append([d[0],d[1]])

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
                if float(occurence)/float(totalCount) >= float(minSup) and pairSet not in freqSet:
                    freqSet.append(pairSet)
                    previousfreqSet.append(pairSet)
                    tempSet = list(pairSet)
                    tempSet.append(occurence)
                    supportSet.append(tempSet)
                    break
#Loops through the frequency list to find L3, L4...
boolean = True
while boolean:
    boolean = False
    addedSet = []
    #For each frequency set in the previous level, add another item to the set
    for k in previousfreqSet:
        for l in firstSet:
            newSet = list(k)
            if l not in newSet:
                newSet.append(l)
                newCount = 0
                #Counts the occurence of the sets intersection {a,b,c,...}
                for n in data:
                    for m in newSet:
                        if n[columns.index(m)] == dataTrue:
                            verify = True
                        else:
                            verify = False
                            break
                    if verify:
                        newCount = newCount + 1
                #If the occurence of the relation is greater than minSup, adds it to the frequency data
                if float(newCount)/float(totalCount) >= float(minSup):
                    freqSet.append(newSet)
                    addedSet.append(newSet)
                    
                    tempSet = list(newSet)
                    tempSet.append(newCount)
                    supportSet.append(tempSet)
                    boolean = True
    #Clears out the level before and adjusts the level
    previousfreqSet = []
    previousfreqSet = addedSet
#Cleans the data to remove duplicates
sortedFreq = [frozenset(o) for o in freqSet]
cleanFreq = set(sortedFreq)


testCount = 0
for j in cleanFreq:
    print list(j)
    testCount =  testCount + 1
print testCount

end = timeit.default_timer()
print "Runtime: ", end - timer
