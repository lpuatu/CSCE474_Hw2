from scipy.io import arff
from array import *
#The Apriori Algorithm for a given file

def genereateRules(minsupport, minconfidence):
    return ""

def generateSubItemsets(minsupport, minconfidence, data, columns, data_list):
    # count = 1;
    # for i in range(len(data_list)):
    #     for j in range(len(data)):
    #         if data[j][data_list[i]]:

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
                tempTup.append([i,columns[i],k,tempCol.count(k), tempCol.count(k)/len(data)])
        data_dict[columns[i]] = tempCol
        data_list.append(tempTup)
    #For data_list it is [name, value, number of times in elements in data, support]
    # print(data_list)
    print("Minimum support: " + minsupport)
    print("Minimum confidence: " + minconfidence + "\n")
    print("Size of large itemset L(1): "+str(len(data_list)))
    print(data_list)
    

if __name__ == "__main__":
    main()
