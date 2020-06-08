-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: giardino_botanico
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB

DROP DATABASE IF EXISTS `giardino_botanico`;
CREATE DATABASE `giardino_botanico`;
USE `giardino_botanico`;


--
-- Table structure for table `ZonaGiardino`
--

DROP TABLE IF EXISTS `ZonaGiardino`;
CREATE TABLE `ZonaGiardino` (
  `id_zona` int(3) NOT NULL AUTO_INCREMENT,
  `numero_zona` int(3) NOT NULL,
  `visitabile` boolean DEFAULT 0,
  PRIMARY KEY (`id_zona`)
) COMMENT="identifica le varie zone del giardino, specificando se sono accessibili o meno al pubblico.";


--
-- Table structure for table `Pianta`
--

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
  PRIMARY KEY (`id_tipo_pianta`),
  UNIQUE KEY `nome_pianta` (`nome_pianta`),
  UNIQUE KEY `nome_pianta_latino` (`nome_pianta_latino`)
) COMMENT="contiene tutte le tipologie di pianta presenti nel giardno ";


--
-- Table structure for table `Pianta`
--

DROP TABLE IF EXISTS `Pianta`;
CREATE TABLE `Pianta` (
  `id_pianta` int(11) NOT NULL AUTO_INCREMENT,
  `tipologia_pianta` int NOT NULL,
  `giorno_piantumazione` date DEFAULT NULL,
  `viva` boolean DEFAULT 1,
  `zona_giardino` int(3) NOT NULL,
  PRIMARY KEY (`id_pianta`),
  CONSTRAINT `pianta_ibk_1` FOREIGN KEY (`tipologia_pianta`) REFERENCES `TipologiaPianta` (`id_tipo_pianta`) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT `pianta_ibk_2` FOREIGN KEY (`zona_giardino`) REFERENCES `ZonaGiardino` (`id_zona`) ON UPDATE CASCADE ON DELETE CASCADE
) COMMENT="contiene informazioni ogni painta del giardino";


