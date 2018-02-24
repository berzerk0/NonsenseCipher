cat *  | tr 'A-Z' 'a-z' | tr '.' '\n' | tr ',' '\n' | tr ' ' '\n' | tr '?' '\n'| tr '!' '\n' | tr -d [[:blank:]]  | tr -d '\r' | egrep '[a-z]' > corpus.txt
