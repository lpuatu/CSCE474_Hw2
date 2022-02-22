from scipy.io import arff
from array import *
#The Apriori Algorithm for a given file

def genereateRules(minsupport, minconfidence):
    return ""

def generateItemsets(minsupport, minconfidence):
    return ""

def main():
    minsupport = input("What is the minimum support for this data?\n")
    minconfidence = input("What is the minimum confidence for this data\n")
    filename = input("What is the filename for this data. Note that it must be in arff format, and the same directory as Apriori.py\n")
    print(minsupport)
    print(minconfidence)
    #loadarff supermarket.arff
    data, meta = arff.loadarff(filename)
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
        print(x)

if __name__ == "__main__":
    main()
