for files in ./*protein*
do
  echo $files >> TabulatedValues.csv
  for file in ./hmmfiles/*
  do
    #./hmmbuild tempStore.fasta $file
    echo $file >> TabulatedValues.csv
    ./hmmsearch --tblout hmm.hits $file $files
    cat hmm.hits | grep -v "#" | wc -l >> TabulatedValues.csv
    echo "" >> TabulatedValues.csv
  done 
done

