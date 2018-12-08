# iterate over files ending in *align.fasta
for filename in *align.fasta
do
    #make a variable of the same name except it ends it ".hmm"
	newname=$(echo $filename | sed s/.fasta/.hmm/)
    # build a hidden markov model based off of the alignment and store with the above name
	./hmmbuild $newname $filename
done
