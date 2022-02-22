from scipy.io import arff
from array import *
import collections
#The Apriori Algorithm for a given file

def genereateRules(minsupport, minconfidence):
    return ""

def generateItemsets(minsupport, minconfidence):
    return ""

# def dataRowsToColumns(data,meta):
#     for 

def main():
    minsupport = input("What is the minimum support for this data?\n")
    minconfidence = input("What is the minimum confidence for this data\n")
    filename = input("What is the filename for this data. Note that it must be in arff format, and the same directory as Apriori.py\n")
    # print(minsupport)
    # print(minconfidence)
    #loadarff supermarket.arff
    data, meta = arff.loadarff(filename)
    data_list = []
    data_dict = {}
    id = 0
    # print(data)
    columns =[]
    
    for f in meta:
        columns.append(f)

    for i in range(len(columns)):
        tempCol = []
        
        for j in range(len(data)):
            tempCol.append(data[j][i])
        tempSet = set(tempCol)
        tempTup = []
        for k in tempSet:
            if tempCol.count(k)/len(data) > float(minsupport):
                tempTup.append([columns[i],k,tempCol.count(k), tempCol.count(k)/len(data)])
        data_dict[columns[i]] = tempCol
        data_list.append(tempTup)
    #For data_list it is [name, value, number of times in elements in data, support]
    # print(data_list)
    print(data_list)
    


    


    # for i in range(len(data)):s
    #     for j in range(data[i]):
        
    # for i in range(len(meta)):
    #     print(meta[i])

    # for f in meta:
    #     itemSet.insert(id, [f, 0])
    #     id = id + 1

    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         if data[i][j] == 't':
    #             count = itemSet[j][1]
    #             itemSet[j][1] = count + 1

    # for x in itemSet:
    #     print(x)

if __name__ == "__main__":
    main()
