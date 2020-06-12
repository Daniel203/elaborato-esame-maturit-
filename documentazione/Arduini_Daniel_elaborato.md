# Arduini Daniel

### 1. Analisi

http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx?basic=s

Un giardino botanico vuole realizzare un sito web in cui gli utenti possano visuallizzare le piante presenti e le loro caratteristiche.

Alcune caratteristiche fondamentali sono sicuramente il nome, sia quello commerciale che quello latino, la specie a cui appartiene, informazioni riguardo alla manutenzione necessaria.

Per realizzare ciò è necessario collegare il sito ad un database contenente tutte queste informazioni.

Il database deve essere divisio in tre tabelle: 

- **TipologiaPianta**: indica il tipo di pianta e le sue caratteristiche

- **Pianta**: rappresenta ogni singola pianta del giardino, con delle caratteristiche specifiche coma la data di piantumazione

- **ZonaGiardino**: contiene le varie zone del giardino e dice se sono accessibili

Una pianta ha diverse caratteristiche che la contraddistinguono: il nome per primo, che può essere sia quello commerciale che quello latino, la specie a cui appartiene, il periodo in cui fiorisce, il colore dei fiori, la manuntenzione che richiede, la quantità di acqua.

Poi nella delle specie, le informazioni importanti sono il nome della specie e alcune caratteristiche che la differenziano dalle altre.

Per ultima la tabella delle zone contiene il nome della zona e un valore che indichi se è o meno aperta al pubblico. Infatti nelle zone del giardino ci sono luoghi non accessibili al pubblico che però non ha senso inserire in un altra tabella.

Una tipologia di pianta può essere esposta in varie zone del giardino, quindi la relazione tra la tabella delle piante e quella delle zone deve essere una molti-a-molti.

Per il sito internet è importante avere una funzione di ricerce delle piante, in modo da poterle trovare facilmente.

Una volta effettuata la ricerca, ogni risultato dovrebbe riportare le informazioni principali della pianta, come nome e specie e sarebbe utile visualizzare anche un'immagine di essa.

Poi cliccando sul risultato sarà possibile visuallizzare in modo approfondito le informazioni della pianta, potendo anche sapere in quale zona del giardino è posizionata.

### 2. Modello  concettuale e logico

Piante(<u>nomePianta</u>, nomeLatino, specie, altezza, inzioFioritura, fineFioritura, area, ),

Specie(<u>nomeSpecie</u>, nomeLatino, clima, origine),

AreaGiardino(<u>NomeArea,</u> ampiezza),

giorno in cui è stata piantata, viva o morta, numero piante

![elaborato_schema_er.png](/home/daniel/Downloads/elaborato_schema_er.png)
