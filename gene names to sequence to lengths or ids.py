# page 155 of manual Enteres search

# Imports module, signs with registered email
from Bio import Entrez 
Entrez.email = "************"

#MADE FOR NUCCORE BUT OTHER DBS WORK NOT SO WELL THOUGH

seqOnly = input("Enter A for all annotations or B for or ID, Length and Sequence Only")

db="nuccore"
halfTerm = "ALS1s4"
term = "APOE"


#Genome gets the size of genes and other interesting facts, can alternate this and sort it if needed
#TODO
#TODO
#TODO
#TODO
#DO THE ABOVE 

# This can be changed to different searches to get different info



handle = Entrez.egquery(term=term)
# If more than one entered put in AND between the arguments
record = Entrez.read(handle)
# The below block will run and return the number of hits in the database
for row in record["eGQueryResult"]:
    if row["DbName"]==db:
        print(row["Count"])

# Prints all the ID's from the search
handle = Entrez.esearch(db=db, term=term)
record = Entrez.read(handle)
gi_list = record["IdList"]
print(gi_list)


# This will print all the data from all the ID's accessed above
gi_str = ",".join(gi_list)
handle = Entrez.efetch(db=db, id=gi_str, rettype="gb", retmode="text")
# If you want to look at the raw GenBank ﬁles, you can read from this handle and print out the result:
text = handle.read()
print(text)

# Sort the data and present it in a more pythonic manner

# p156
from Bio import SeqIO
handle = Entrez.efetch(db=db, id=gi_str, rettype="gb", retmode="text")
records = SeqIO.parse(handle, "gb")
#We can now step through the records and look at the information we are interested in:


#This prints the summary annotations only anyway regardless of what is entered
if seqOnly == "A":
    for record in records:
    #the below prints all the details
        print("%s, length %i, with %i features, description: %s, sequence: %s" % (record.name, len(record), len(record.features), record.description, record.seq))
    #belw here just does name aand sequence
if seqOnly == "B":
    for record in records:
        print("name ", record.name, "length", len(record), "sequence ", record.seq)
