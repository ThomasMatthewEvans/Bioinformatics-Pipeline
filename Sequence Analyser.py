# Opens a csv file and prints the first row
# This will be used to parse csv files from script to script
from Bio import Entrez                       # Imports module, signs with registered email
from Bio.Seq import Seq
from Bio import Align
import csv
from Bio import pairwise2                   # Import pairwise2 module
from Bio.pairwise2 import format_alignment  # Import format_alignment method
from Bio.Alphabet import IUPAC
import pandas as pd                         # Uses pands for list conprehension also
Entrez.email = "*************"

#TODO

#1 Ask if user wants alignments assessed
#2 Ask if user wants complementary starands assessed
#3 Ask if used wants RNA Made
#4 Ask if they want to count specific things in the DNA i.e. C to G etc

with open("FS.csv") as f:                    # Opens the csv file
    for row in f:                           # Iterates over each row and prints it
        print (row)

df = pd.read_csv("FS.csv")                   # Read the csv in pandas
#Then, getting the first column is as easy as:
matrix = df[df.columns[0]].as_matrix()      # Creates a matrix with the first column from the csv only
myList = matrix.tolist()

print(myList)                               # previous are QC Tests, can be deleted once run
print(myList[0])

#aS = TTCTCTGTTCCTGTTGGCCCAAAATACAAAGCTGTACAGCAACATGGATGGTACAACAAGTTTATTTGAGGCAAGTATCTTCTCTGGGAGACAAATACAGACACAGACACACACACACACAGTACAGCATAAACAGTGCTTCGTCTATACATCGCTAGGTAACTGATTATAGTCAGTAGCTAGGATATCTGCGAATCGGATTAGGATGCCATGAAAAGTAAACCTTTGTGGACTGAGAGCACAGGAGGGACTGGGATAGCTCA
#aligner = Align.PairwiseAligner

csvIterator = 0
csvIteratorCap = len(myList)
# print(csvIteratorCap)                     QC Test - Archived
# csvIterator = csvIterator + 1             QC Test - Archived
#iterate over the sequences and alter them in some way
#----ALIGNMENT BLOCK-------#
#Alignment Block - put in a input question to do this
while csvIterator < csvIteratorCap:
    mySeq = myList[csvIterator]
    mySeq = str(mySeq)
    X = "TTCTCTGTTCCTGTTGGCCCAAAATACAAAGCTGTACAGCAACATGGATGGTACAAC"                         #Alignment Sequence
    # Get a list of the global alignments between the two sequences ACGGGT and ACG # No parameters. Identical characters have score of 1, else 0. # No gap penalties.
    alignments = pairwise2.align.globalxx(X, mySeq)
    # Use format_alignment method to format the alignments in the list
    for a in alignments:
        print(format_alignment(*a))
    #Call the iterator function we need
    csvIterator = csvIterator + 1

#----COMPLEMENTARY STRAND BLOCK-------#
#Makes complementary strand - NOT REVERSED strand!
print("AAAAA")                                  # QC Test
csvIterator2 = 0
csvIteratorCap2 = len(myList)
while csvIterator2 < csvIteratorCap2:
    mySeq = myList[csvIterator2]
    myS = Seq(mySeq)                            #Creates a Sequence object out of the sequence of interest
    complementrySeq = myS.complement()          #Creates the complementry strand and prints it
    print(complementrySeq)
    csvIterator2 = csvIterator2 + 1             #Moves to the next sequence and revisits the while loop start


#Get specfic positions in the DNA



#A = "AAAAA"                                    #Archived QC Test
#B = "AA"
#F=A.count(B)
#print(F)

#--------COUNT MOTIFS-----------------#
csvIterator3 = 0
csvIteratorCap3 = len(myList)
while csvIterator3 < csvIteratorCap3:
    mySeq = myList[csvIterator3]
    mySeq = str(mySeq)
    B = "TTCTCTGTTCCTGTTGGCCCAAAATACAAAGCTGT"
    countMotifs = mySeq.count(B)
    print(countMotifs)
    csvIterator3 = csvIterator3 + 1
#
#
#
#
#
#RIP off p 22 of book




# Define two sequences to be aligned
# searching for sequences in the DNA is first
# Create function to search sequence, put it above the iterator cal it when needed


#converting the DNA to RNA etcht ehn searhcing it

#p24 in biopython cookbook
