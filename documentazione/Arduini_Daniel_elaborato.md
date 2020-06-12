# Arduini Daniel

### 1. Analisi

Un giardino botanico vuole realizzare un sito web in cui gli utenti possano visuallizzare le piante presenti e le loro caratteristiche.

Alcune caratteristiche fondamentali sono sicuramente il nome, sia quello commerciale che quello latino, la specie a cui appartiene, informazioni riguardo alla manutenzione necessaria.

Per realizzare ciò è necessario collegare il sito ad un database contenente tutte queste informazioni.

#### Database

Il database deve essere divisio in tre tabelle: 

- **TipologiaPianta**: indica il tipo di pianta e le sue caratteristiche come il periodo di fiortura, la manuntenzione necessaria ...

- **Pianta**: rappresenta ogni singola pianta del giardino, con delle caratteristiche specifiche coma la data di piantumazione, luogo in cui è posizionata all'interno del giardino

- **ZonaGiardino**: contiene le varie zone del giardino e dice se sono accessibili al pubblico

#### Sito web

Il sito web nella home page deve presentare le varie tipologie di pianta, ordinate alfabeticamente, insieme ad una funzione "cerca", in modo da facilitare l'identificazione di un determinato risultato.

Una volta selezionata una tipologia di piante, il sito deve portare ad una pagina con un altra tabella in cui vengono mostrate tutte le piante di quel tipo, insieme ad alcune caratteristiche più specifiche come il giorno di piantumanzione e l'apertura al pubblico.

Infine selezionata la pianta devono essere mostrati tutti i dettagli di essa.

























## 2. Modello  concettuale e logico

![elaborato_schema_er.png](/home/daniel/Desktop/elaborato/documentazione/elaborato_schema_er.png)

![elaborato_schema_logico.png](/home/daniel/Desktop/elaborato/documentazione/elaborato_schema_logico.png)



## 3. Implementazione della base di dati

#### TipologiaPianta

```sql
DROP TABLE IF EXISTS `TipologiaPianta`;
CREATE TABLE `TipologiaPianta` (
  `id_tipo_pianta` int(11) NOT NULL AUTO_INCREMENT,
  `nome_pianta` varchar(50) NOT NULL,
  `nome_pianta_latino` varchar(50) DEFAULT NULL,
  `nome_specie` varchar(50) NOT NULL,
  `inizio_fioritura` enum('Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre', 'non fiorisce', 'stagionale') DEFAULT NULL,
  `fine_fioritura` enum('Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre', 'non fiorisce', 'stagionale') DEFAULT NULL,
  `acqua_necessaria` enum('poca','media','tanta') DEFAULT NULL,
  `manutenzione_necessaria` enum('poca','media','tanta') DEFAULT NULL, 
  PRIMARY KEY (`id_tipo_pianta`)
) COMMENT="contiene tutte le tipologie di pianta presenti nel giardno ";
```

```sql
INSERT INTO `ZonaGiardino` (`numero_zona`, `visitabile`)
VALUES
  (10, true),
  (1, false),
  (19, true),
  (102, true),
  (98, false);
```

#### ZonaGiardino

```sql
DROP TABLE IF EXISTS `ZonaGiardino`;
CREATE TABLE `ZonaGiardino` (
  `id_zona` int(3) NOT NULL AUTO_INCREMENT,
  `numero_zona` int(3) NOT NULL,
  `visitabile` boolean DEFAULT 0,
  PRIMARY KEY (`id_zona`)
) COMMENT="identifica le varie zone del giardino, specificando se sono accessibili o meno al pubblico.";
```

```sql
INSERT INTO `TipologiaPianta` (`nome_pianta`, `nome_pianta_latino`, `nome_specie`, `inizio_fioritura`, `fine_fioritura`, `acqua_necessaria`, `manutenzione_necessaria`)
VALUES 
  ('Carciofo', 'Cynara cardunculus', 'Cynara', 'stagionale', 'stagionale', 'media', 'poca'),
  ('Cipresso comune', 'Cupressus sempervirens', 'Cupressaceae', 'non fiorisce', 'non fiorisce', 'media', 'media'),
  ('Quercia rossa', 'Quercus rubra', 'Fagaceae', 'Maggio', 'Giugno', 'tanta', 'poca'),
  ('Maonia', 'Mahonia aquifolium', 'Berberidaceae', 'Aprile', 'Maggio', 'media', 'media'),
  ('Ippocastano', 'Aesculus hippocastanum', 'Hippocastanaceae', 'Maggio', 'Giugno', 'media', 'media');
```

#### Pianta

```sql
DROP TABLE IF EXISTS `Pianta`;
CREATE TABLE `Pianta` (
  `id_pianta` int(11) NOT NULL AUTO_INCREMENT,
  `tipologia_pianta` int NOT NULL,
  `giorno_piantumazione` date DEFAULT NULL,
  `viva` boolean DEFAULT 1,
  `zona_giardino` int(3) NOT NULL,
  `immagine` varchar(100) DEFAULT NUll,
  PRIMARY KEY (`id_pianta`),
  CONSTRAINT `pianta_ibk_1` FOREIGN KEY (`tipologia_pianta`) REFERENCES `TipologiaPianta` (`id_tipo_pianta`) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `pianta_ibk_2` FOREIGN KEY (`zona_giardino`) REFERENCES `ZonaGiardino` (`id_zona`) ON UPDATE CASCADE ON DELETE CASCADE
) COMMENT="contiene informazioni ogni painta del giardino";
```

```sql
INSERT INTO `Pianta` (`tipologia_pianta`, `giorno_piantumazione`, `viva`, `zona_giardino`, `immagine`)
VALUES 
  ('1', '2019-12-04', true, 1, 'immagine1'),
  ('1', '2017-12-04', false, 5, 'immagine2'),
  ('2', '2009-09-27', true, 2, 'immagine3'),
  ('3', '2003-06-12', false, 3, 'immagine4'),
  ('4', '2007-04-18', true, 2, 'immagine5'),
  ('5', '2009-10-30', false, 5, 'immagine6');
```

#### Query SQL

#### Query 1

Ottiene i nomi di tutte le piante che sono vive, ma non sono visitabili dal pubblico.

```sql
SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie 
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE p.viva = true AND zg.visitabile = false;
```

#### Query 2

Torva i nomi di tutte le piante che fioriscono nel mese di maggio

```sql
SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie 
FROM TipologiaPianta AS tp 
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
WHERE tp.inizio_fioritura = 'MAGGIO' OR tp.fine_fioritura = 'MAGGIO';
```


