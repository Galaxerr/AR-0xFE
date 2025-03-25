La challenge è divisa in 4 fasi:

1. Il primo video ha nella descrizione un blocco di testo codificato in base64 un po' di volte,
mettendolo su cyberchef si rivela l'url ad un sito fatto con flask, in cui è evidente l'aggiunta di
una path traversal tramite l'immagine di background. La soluzione quindi è semplicemente
navigare indietro di cartelle fino a trovare il file flag.txt.

filename=../../../../../../flag.txt

2. Questa volta, la descriione non dà nessuna informazione utile, mentre l'audio del video si nota essere diverso dal normale, per cui
la flag sarà contenuta all'interno di questo. L'audio è fornito negli attachments (perché usare un sito "youtube to mp3" non funzionava).
Una volta ottenuto il file audio, lo si può mettere su audacity e visualizzarne lo spettrogramma per rivelare
una password, necessaria ad ottenere la flag: ciaomamma123.
A questo punto, bisogna estrarre la flag dall'audio, facendo una semplice estrazione di file da cyberchef
o, più correttamente, utilizzando il comando:

    steghide extract -sf NOME_FILE.wav

La password per estrarre è la stessa che serve per unzippare la flag. a questo punto il file flag.txt
contiene il link per la prossima fase.

3. Il video non contiene nulla di particolare, la descrizione invece fa vedere una stringa criptata con il cifrario di cesare,
bruteforceabile tranquillamente, per rivelare il comando netcat a cui connettersi per la challenge.
Il servizio non è altro che un semplice gioco di tris con un bot, in cui vincere, pareggiare o perdere non cambia nulla,
ma scrivendo HELP al posto di uno dei simboli, esce in maiuscolo la sola parola SECRET, indicando al fatto
di dover scrivere SECRET al posto di uno dei simboli per attivare la modalità segreta.
In questa modalità si può giocare con un'altra persona, ma il vero obiettivo è quello di riempire tutte le
celle dello stesso simbolo, come si poteva capire vagamente dall'aiuto.
Selezionato un simbolo quindi, si possono scrivere tutti i numeri delle celle separati da spazio
per riempire completamente il campo da gioco, rivelando quindi l'ultimo video

4. Il video fa vedere una parola sola, che da sola non serve a nulla, invece la descrizione mostra chiaramente
il link ad un altro sito. Navigandoci, troveremo le indicazioni per ottenere la flag, che fanno capire
che in ognuno dei video di ciascuna fase è presente una parola nascosta, che unite nell'ordine delle fasi
rivelano la password da inviare al sistema per mostrare la flag finale 

Password: Y0u_4c7u4lly_D1d_I7_Y0u_M4d7l4d

Flag: UNIFE{C0n6r47z_On_834t1ng_7h3_ARG}
