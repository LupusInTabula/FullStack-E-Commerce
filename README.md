Libraries: Pillow, Psycopg2, Bootstrap, JQuery, Whitenoise, Gunicorn, Unicorn, Dj-database-url

Il sito include funzionalità di gestione di login e singin dell'utente, gestione del carello e dell'ordine:
l'utente può registrarsi al sito attraverlo l'apposito bottone in alto a destra, dopo viene rendirizzato alla pagina
login. Una volta effettuato l'accesso per vedere che sia andato a buon fine il sito presenterà una scritta 'Wealcome %user%'.
All'interno del sito è possibile aggiungere elementi al carrello solo se l'accesso è stato effettuato, altrimenti al posto di un bottone
'add to cart' verra visualizzata una scritta 'Login to add to cart'.
Inoltre è possibile effettuare il logout dal sito. Ogni utente ha un suo carrello personale che può gestire. Il carrello viene visualizzato sulla sinistra,
in modalità desktop, in alto sotto l'header, in modalità device. Il carrello è dotato di proprietà sticky in modo che l'utente
possa tenere sotto controllo il carrello in ogni momento. In qualsiasi momento è possibile rimuore elementi dal carrello cliccando sul tasto 'remove'.
Cliccando sull'icona del carrello l'utente viene renderizzato alla pagina di gestione dell'ordine. Qui l'utente può rimuovere gli articoli dal carrello
oppure confermare l'ordine, questo comporta la diminuzione degli articoli dallo stock nonchè un pop-up comunicante che il carrello è stato svuotato 
e il totale da pagare.
Vi è anche implementata una funzione di ricerca tramite search bar in alto a sinistra che permette di cercare all'interno dello store gli articoli per nome.
