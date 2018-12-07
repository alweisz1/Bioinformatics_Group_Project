# Import the necessary tools to operate on alignment data
import numpy as np
import pandas as df

# Import the alignment data as a dataframe
data = df.read_table('ZS66BHFH014-Alignment-HitTable.csv',header=None)



# Takes the first column of the alignment data and makes it a list
# This is useful for iterating over, I'm just familiar with list indexing I guess
val = list(data.iloc[:,0])


# The way this loop works is by "catching" each change in the title, that is by pulling out the first 
# Part of the first position. In this case "Transcipt#..." and by doing so, knowing that the first gene
# to show for each Transcript is what we want, we can just pull the second item out from whatever
# new "Transcript#..." has not been encountered yet

# Name of genes
names = []

# Name of Transcript
titles = []

# Iterate over the first column of data
for item in val:
    
    # parse away the pesky delimiters
    stuff = item.split(',')
    
    # see if this is the first instance of finding this "Transcript#..."
    if stuff[0] not in titles:
        
        # if so, add the Transcript name and gene to their respective lists
        titles.append(stuff[0])
        names.append(stuff[1])

# sanity check to make sure the 6 transcripts were iterated over appropriately
print titles
    


### this is the list of top 6 amino acids
print names

