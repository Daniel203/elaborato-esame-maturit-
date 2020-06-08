USE `giardino_botanico`;


--
-- dump for table `TipologiaPianta`
--

INSERT INTO `TipologiaPianta` (`nome_pianta`, `nome_pianta_latino`, `nome_specie`, `inizio_fioritura`, `fine_fioritura`, `acqua_necessaria`, `manutenzione_necessaria`)
VALUES 
  ('Carciofo', 'Cynara cardunculus', 'Cynara', 'stagionale', 'stagionale', 'media', 'poca'),
  ('Cipresso comune', 'Cupressus sempervirens', 'Cupressaceae', 'non fiorisce', 'non fiorisce', 'media', 'media'),
  ('Quercia rossa', 'Quercus rubra', 'Fagaceae', 'Maggio', 'Giugno', 'tanta', 'poca'),
  ('Maonia', 'Mahonia aquifolium', 'Berberidaceae', 'Aprile', 'Maggio', 'media', 'media'),
  ('Ippocastano', 'Aesculus hippocastanum', 'Hippocastanaceae', 'Maggio', 'Giugno', 'media', 'media');


--
-- dump for table `ZonaGiardino`
--

INSERT INTO `ZonaGiardino` (`numero_zona`, `visitabile`)
VALUES
  (10, true),
  (1, false),
  (19, true),
  (102, true),
  (98, false);


--
-- dump for table `Pianta`
--

INSERT INTO `Pianta` (`tipologia_pianta`, `giorno_piantumazione`, `viva`, `zona_giardino`)
VALUES 
  ('1', '2019-12-04', true, 1),
  ('2', '2009-09-27', true, 2),
  ('3', '2003-06-12', false, 3),
  ('4', '2007-04-18', true, 2),
  ('5', '2009-10-30', false, 5);
