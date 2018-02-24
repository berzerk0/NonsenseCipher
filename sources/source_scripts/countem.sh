for i in $(seq 1 5)
do
	egrep "^.{$i}$" corpus.txt | wc -l
done
