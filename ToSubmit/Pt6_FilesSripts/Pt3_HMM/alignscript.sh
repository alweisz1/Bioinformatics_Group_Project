# iterate over all files of the form "Sequence*.fasta" in the current directory
for filename in Sequence*.fasta
do
    #make a variable that has the same name as the original files but now with ".align" appended
	newname=$(echo $filename | sed s/.fasta/align.fasta/) 
    # perform a muscle alignment on the sequence and store it with the above name
	./muscle3.8.31_i86linux64 -in $filename -out $newname
done
