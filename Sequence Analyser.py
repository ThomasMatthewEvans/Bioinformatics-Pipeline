#TODO
# IMPORT DAFA FROM CSV OR NET
# Create functions to print the SEQUENCE,rna dna look for bits and MORE, each
#BECALLABE, EXPORTAS CSV 
# Opens a csv file and prints the first row
# This will be used to parse csv files from script to script
from Bio import Entrez                       # Imports module, signs with registered email
from Bio.Seq import Seq
import csv
import pandas as pd                         # Uses pands for list conprehension also
Entrez.email = "t-m-evans@hotmail.com"

with open("a.csv") as f:                    # Opens the csv file
    for row in f:                           # Iterates over each row and prints it
        print (row)

df = pd.read_csv("a.csv")                   # Read the csv in pandas
#Then, getting the first column is as easy as:
matrix = df[df.columns[0]].as_matrix()      # Creates a matrix with the first column from the csv only
myList = matrix.tolist()

print(myList)                               # previous are QC Tests, can be deleted once run
print(myList[0])

csvIterator = 0
csvIteratorCap = len(myList)
# print(csvIteratorCap)                     QC Test - Archived
csvIterator = csvIterator + 1

#iterate over the sequences and alter them in some way


#searching for sequences in the DNA is first


#converting the DNA to RNA etcht ehn searhcing it




