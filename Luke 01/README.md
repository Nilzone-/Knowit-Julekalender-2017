**Oppgave 1**

Bigram og trigram er eksempler på to spesifikke n-gram, med henholdvis n=2 og n=3.

For ordet snowflake lages bigrammene (n=2): sn, no, ow, wf, fl, la, ak, ke. Som sammensatt blir snnoowwffllaakke.

Tilsvarende for ordet mistletoe lages trigrammene (n=3): mis, ist, stl, tle, let, eto, toe. Som sammensatt blir misiststltleletetotoe.

Hvis det sammensatte ordet blir permutert i en tilfeldig rekkefølge lages det et n-gram-anagram.

Eksempelvis er fnaewkfonklsawlo et 2-gram-anagram av snowflake, mens itseotltmlelteoitetss er et 3-gram-anagram av mistletoe.

Hvilket ord fra denne ordlisten ble brukt til å lage det følgende n-gram-anagrammet, og hva er verdien for n?

aeteesasrsssstaesersrrsse

Svarformat: <n>-<ord fra ordlisten>

Eksempelvis for 'itseotltmlelteoitetss' fra ovenfor er svaret: 3-mistletoe

Hint: Du kan hente ordlisten som følger

curl https://s3-eu-west-1.amazonaws.com/julekalender-knowit-2017-vedlegg/wordlist.txt -O
