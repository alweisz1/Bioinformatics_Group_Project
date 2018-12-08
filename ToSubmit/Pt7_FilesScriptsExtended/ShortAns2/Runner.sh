
# make the muscle alignments for the two proteins

./muscle3.8.31_i86linux64 -in sequenceNOT.fasta -out hmmNOTPrimate.fasta

./muscle3.8.31_i86linux64 -in sequencePRIMATE.fasta -out hmmPrimate.fasta

./hmmbuild seqNOT.hmm hmmNOTPrimate.fasta

./hmmbuild seqPrimate.hmm hmmPrimate.fasta

./hmmsearch --tblout hmm01.hits seqNOT.hmm Control1protein.fasta

cat hmm01.hits | grep -v "#" | wc -l >> TabulatedNOT.csv

./hmmsearch --tblout hmm02.hits seqPrimate.hmm Control1protein.fasta

cat hmm02.hits | grep -v "#" | wc -l >> TabulatedPrimate.csv
