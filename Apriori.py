from scipy.io import arff
from array import *
#The Apriori Algorithm for a given file

def genereateRules(minsupport, minconfidence):
    return ""

def generateSubItemsets(minsupport, minconfidence, data, columns, data_list):
    #data list [0] is position in columns data list [2] is the value of that it has
    count = 1
    


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
        data_list.extend(tempTup)
    #For data_list it is [number,name, value, number of times in elements in data, support]
    # print(data_list)
    print("Minimum support: " + minsupport)
    print("Minimum confidence: " + minconfidence + "\n")
    print("Size of large itemset L(1): "+str(len(data_list)))
    print(data_list)
    
    
    secondlist = []
    for x in range(len(data_list)):
        for y in range(x,len(data_list)):
            supconcount = 0
            if (x != y):
                for i in range(len(data)):
                    #The element that has to change is the data_list[x][0] and data_list[y][0]
                    
                    if ((data[i][data_list[x][0]] == data_list[x][2]) and (data[i][data_list[y][0]] == data_list[y][2])):
                        supconcount += 1
                support = supconcount/len(data)
                if(support > float(minsupport)):
                    secondlist.append([data_list[x],data_list[y],support])
    print("Size of large itemset L(2):" +str(len(secondlist)))
    print(secondlist)
        
    

if __name__ == "__main__":
    main()
