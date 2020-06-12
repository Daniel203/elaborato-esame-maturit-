USE `giardino_botanico`

--
-- ottieni i nomi di tutte le piante che sono vive, ma non sono visitabili
--

SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie 
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE p.viva = true AND zg.visitabile = false;


--
-- ottieni i nomi di tutte le piante che fioriscono nel mese di maggio 
--

SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie 
FROM TipologiaPianta AS tp 
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
WHERE tp.inizio_fioritura = 'MAGGIO' OR tp.fine_fioritura = 'MAGGIO';
