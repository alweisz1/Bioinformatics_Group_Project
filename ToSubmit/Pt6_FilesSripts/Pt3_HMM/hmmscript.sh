for filename in *align.fasta
do
	newname=$(echo $filename | sed s/.fasta/.hmm/)
	./hmmbuild $newname $filename
done
