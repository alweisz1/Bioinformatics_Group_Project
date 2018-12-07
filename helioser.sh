# iterate over all of the files in the directory that contain the string "protein" (RNA seqs)
for files in ./*protein*
do

  #echo $files >> TabulatedValues.csv
  
  # iterate over all of the hmmfiles in ./hmmfiles
  for file in ./hmmfiles/*
  do
    # turn the protein names into a string that can be used to differentiate hmm hits
    stringy=$(cat $files | sed s,.fasta,.csv,g)
    
    # put any first line in the csv to be used as header when imported with pandas
    echo $file >> TabulatedVal$stringy.csv
    # run hmmsearch using hmm file and proteins
    ./hmmsearch --tblout hmm.hits $file $files
    # find the number of hits for each sequence and strore them using the differentiator
    cat hmm.hits | grep -v "#" | wc -l >> TabulatedVal$stringy.csv
    
    # add an extra line at the end to be nice to people that may need to use this code later
    echo "" >> TabulatedVal$stringy.csv
  done 
done

