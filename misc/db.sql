-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cardapios`
--

DROP TABLE IF EXISTS `cardapios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardapios` (
  `ID_Cardapio` int NOT NULL AUTO_INCREMENT,
  `Data` date DEFAULT NULL,
  `Almoco_ID` int DEFAULT NULL,
  `Jantar_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID_Cardapio`),
  KEY `Almoco_ID` (`Almoco_ID`),
  KEY `Jantar_ID` (`Jantar_ID`),
  CONSTRAINT `cardapios_ibfk_1` FOREIGN KEY (`Almoco_ID`) REFERENCES `porcoes` (`ID_Porcao`),
  CONSTRAINT `cardapios_ibfk_2` FOREIGN KEY (`Jantar_ID`) REFERENCES `porcoes` (`ID_Porcao`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardapios`
--

LOCK TABLES `cardapios` WRITE;
/*!40000 ALTER TABLE `cardapios` DISABLE KEYS */;
INSERT INTO `cardapios` VALUES (1,'2022-07-26',2,1),(2,'2022-07-27',4,8),(3,'2022-07-28',1,5),(4,'2022-07-29',6,2),(5,'2022-07-30',5,3),(6,'2022-07-31',5,3),(7,'2022-08-01',7,2),(8,'2022-08-02',6,1);
/*!40000 ALTER TABLE `cardapios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estoque`
--

DROP TABLE IF EXISTS `estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estoque` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Ingrediente` varchar(50) DEFAULT NULL,
  `Quantidade` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estoque`
--

LOCK TABLES `estoque` WRITE;
/*!40000 ALTER TABLE `estoque` DISABLE KEYS */;
INSERT INTO `estoque` VALUES (1,'Arroz',800),(2,'Feijão Carioca',600),(3,'Carne Bovina',450),(4,'Carne Suína',400),(5,'Feijão Preto',700),(6,'Macarrão',500),(7,'Alface',300),(8,'Batata',600),(9,'Lombo',800),(10,'Repolho',300),(11,'Farofa',300),(12,'Couve',400),(13,'Batata Palha',600),(14,'Peito de Frango',900),(15,'Tomate',200),(16,'Milho',200),(17,'Frango',600),(18,'Nabo',250);
/*!40000 ALTER TABLE `estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `infonutricional`
--

DROP TABLE IF EXISTS `infonutricional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `infonutricional` (
  `Ingrediente_ID` int NOT NULL AUTO_INCREMENT,
  `Ingrediente` varchar(50) DEFAULT NULL,
  `TamanhoPorcao` float DEFAULT NULL,
  `ValorEnergético` float DEFAULT NULL,
  `Carboidratos` float DEFAULT NULL,
  `Proteínas` float DEFAULT NULL,
  `GordurasTotais` float DEFAULT NULL,
  `GordurasSaturadas` float DEFAULT NULL,
  `GordurasTrans` float DEFAULT NULL,
  `FibraAlimentar` float DEFAULT NULL,
  `Sódio` float DEFAULT NULL,
  PRIMARY KEY (`Ingrediente_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infonutricional`
--

LOCK TABLES `infonutricional` WRITE;
/*!40000 ALTER TABLE `infonutricional` DISABLE KEYS */;
INSERT INTO `infonutricional` VALUES (1,'Arroz',50,185,3.4,0,0,0,0,1.4,0),(2,'Feijão Carioca',60,205,38,12,0.6,0,0,11,5),(3,'Carne Bovina',50,145,3.1,6.1,12,1.1,0,0,483),(4,'Macarrão',50,130,40,10,0,0,0,10,300),(5,'Alface',60,100,1,40,0,0,0,5,0),(6,'Batata',150,200,60,20,0,0,0,30,120),(7,'Farofa',100,130,80,15,5,10,0,10,400),(8,'Tomate',40,80,1,50,0,0,0,5,0);
/*!40000 ALTER TABLE `infonutricional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `porcao`
--

DROP TABLE IF EXISTS `porcao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `porcao` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_Porcao` int NOT NULL,
  `Ingrediente_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Ingrediente_ID` (`Ingrediente_ID`),
  CONSTRAINT `porcao_ibfk_1` FOREIGN KEY (`Ingrediente_ID`) REFERENCES `infonutricional` (`Ingrediente_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `porcao`
--

LOCK TABLES `porcao` WRITE;
/*!40000 ALTER TABLE `porcao` DISABLE KEYS */;
INSERT INTO `porcao` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,5),(5,2,1),(6,2,2),(7,2,4),(8,2,5);
/*!40000 ALTER TABLE `porcao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `porcoes`
--

DROP TABLE IF EXISTS `porcoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `porcoes` (
  `ID_Porcao` int NOT NULL AUTO_INCREMENT,
  `Acomp1` varchar(50) DEFAULT NULL,
  `Acomp2` varchar(50) DEFAULT NULL,
  `Guarnicao` varchar(50) DEFAULT NULL,
  `Prato_Principal` varchar(50) DEFAULT NULL,
  `Salada` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Porcao`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `porcoes`
--

LOCK TABLES `porcoes` WRITE;
/*!40000 ALTER TABLE `porcoes` DISABLE KEYS */;
INSERT INTO `porcoes` VALUES (1,'Arroz','Feijão Carioca','Macarrão','Carne Bovina','Alface'),(2,'Arroz','Feijão Carioca','Batata','Lombo','Repolho'),(3,'Arroz','Feijão Preto','Farofa','Carne Suína','Couve'),(4,'Arroz','Feijão Carioca','Batata Palha','Peito de Frango','Tomate'),(5,'Arroz','Feijão Carioca','Milho','Frango','Nabo'),(6,'Arroz','Feijão Preto','Milho','Lombo','Tomate'),(7,'Arroz','Feijão Preto','Batata','Frango','Repolho'),(8,'Arroz','Feijão Carioca','Farofa','Carne Bovina','Alface');
/*!40000 ALTER TABLE `porcoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semana`
--

DROP TABLE IF EXISTS `semana`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semana` (
  `ID_Cardapio` int NOT NULL DEFAULT '0',
  `Data` date DEFAULT NULL,
  `Almoco_ID` int DEFAULT NULL,
  `Jantar_ID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semana`
--

LOCK TABLES `semana` WRITE;
/*!40000 ALTER TABLE `semana` DISABLE KEYS */;
INSERT INTO `semana` VALUES (2,'2022-07-27',4,8),(3,'2022-07-28',1,5),(4,'2022-07-29',6,2),(5,'2022-07-30',5,3),(6,'2022-07-31',5,3),(7,'2022-08-01',7,2),(8,'2022-08-02',6,1);
/*!40000 ALTER TABLE `semana` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Tipo` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'caio','1234','Funcionário'),(2,'luan','capivara','Funcionário'),(3,'olavo','1234','Nutricionista'),(4,'2','23','32'),(8,'nutri','1234','Nutricionista'),(9,'func','capi','Funcionário'),(10,'ff','122','Funcionário'),(11,'ff2','1234','Nutricionista');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-03 13:19:44
