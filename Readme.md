# Fuzz Testing Program

## Required Imports
The program requires 2 imports.
On the CSE/CSCE server these imports should be built in. Otherwise if the imports appear missing on the server they can be installed with:
```bash
pip3 install Scipy.io 
pip3 install array
```
## Running The Program
The program should be run on the CSE server but can be run on any bash shell. This program requires that the file used for the algorithm is in the same directory as the Apriori.py file. The application can be run using the bash command below.
```bash
python3 Apriori.py 
```
Once inside the program a user will be asked for minimum support and confidence. From there they will need to specify an .arff file (including file extension) to use on the algorithm. From there, the algorithm will compute itemsets and rules for the system.
