for files in ./*protein*
do
  for file in ./hmmfiles/*
  do
    #./hmmbuild tempStore.fasta $file
    echo $files >> TabulatedValues.csv
    echo $file >> TabulatedValues.csv
    ./hmmsearch --tblout hmm.hits $file $files
    cat hmm.hits | grep -v "#" | wc -l >> TabulatedValues.csv
    echo "" >> TabulatedValues.csv
  done 
done

