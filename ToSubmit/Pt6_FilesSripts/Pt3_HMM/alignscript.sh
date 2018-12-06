for filename in Sequence*.fasta
do
	newname=$(echo $filename | sed s/.fasta/align.fasta/) 
	./muscle3.8.31_i86linux64 -in $filename -out $newname
done
