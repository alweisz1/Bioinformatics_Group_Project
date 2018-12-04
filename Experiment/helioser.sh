for files in ./protein/*
do
  name2=$(echo $files | sed s,./protein/,,g)
  name=$(echo $name2 | sed s,.fasta,.csv,g)
  for file in ./hmmfiles/*
  do
    #./hmmbuild tempStore.fasta $file
    echo $file >> TabulatedVal$name
    ./hmmsearch --tblout hmm.hits $file $files
    cat hmm.hits | grep -v "#" | wc -l >> TabulatedVal$name
    echo "" >> TabulatedVal$name
  done 
done

