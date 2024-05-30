-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: menu
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `beverages`
--

DROP TABLE IF EXISTS `beverages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beverages` (
  `ITEM` varchar(90) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(90) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beverages`
--

LOCK TABLES `beverages` WRITE;
/*!40000 ALTER TABLE `beverages` DISABLE KEYS */;
INSERT INTO `beverages` VALUES ('TEA',60,'HOT'),('COFFEE',70,'HOT'),('COLD COFFEE',80,'COLD'),('MOCKTAILS',95,'COLD'),('HOT CHOCOLATE',120,'HOT'),('JUICE',80,'COLD'),('LEMONADE',55,'COLD'),('BUDWISER',360,'COLD'),('MINERAL WATER',70,'COLD');
/*!40000 ALTER TABLE `beverages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breakfast`
--

DROP TABLE IF EXISTS `breakfast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breakfast` (
  `ITEM` varchar(20) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breakfast`
--

LOCK TABLES `breakfast` WRITE;
/*!40000 ALTER TABLE `breakfast` DISABLE KEYS */;
INSERT INTO `breakfast` VALUES ('SANDWICH',50,'VEG'),('POHA',80,'VEG'),('IDLI',50,'VEG'),('AALO PARATHA',20,'VEG'),('EGG TOAST',80,'NON-VEG'),('HOT-DOG',120,'NON-VEG'),('FRUIT SALAD',90,'VEG');
/*!40000 ALTER TABLE `breakfast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desert`
--

DROP TABLE IF EXISTS `desert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desert` (
  `ITEM` varchar(20) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desert`
--

LOCK TABLES `desert` WRITE;
/*!40000 ALTER TABLE `desert` DISABLE KEYS */;
INSERT INTO `desert` VALUES ('HOT CHOCKLET',280,'HOT');
/*!40000 ALTER TABLE `desert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desserts`
--

DROP TABLE IF EXISTS `desserts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desserts` (
  `ITEM` varchar(60) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desserts`
--

LOCK TABLES `desserts` WRITE;
/*!40000 ALTER TABLE `desserts` DISABLE KEYS */;
INSERT INTO `desserts` VALUES ('CHOCOLATE CAKE',55,'COLD'),('ICE-CREAM',65,'COLD'),('RAS MALAI',90,'COLD'),('GULAB JAMUN',90,'COLD');
/*!40000 ALTER TABLE `desserts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dinner`
--

DROP TABLE IF EXISTS `dinner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dinner` (
  `ITEM` varchar(90) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dinner`
--

LOCK TABLES `dinner` WRITE;
/*!40000 ALTER TABLE `dinner` DISABLE KEYS */;
INSERT INTO `dinner` VALUES ('NAAN',65,'VEG'),('FISH-FRY',98,'NON-VEG'),('CHICKEN 65',98,'NON-VEG'),('PANEER BUTTER MASALA',150,'VEG'),('PULAO',120,'VEG'),('BIRYANI',150,'NON-VEG');
/*!40000 ALTER TABLE `dinner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lunch`
--

DROP TABLE IF EXISTS `lunch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lunch` (
  `ITEM` varchar(20) DEFAULT NULL,
  `PRICE` int DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lunch`
--

LOCK TABLES `lunch` WRITE;
/*!40000 ALTER TABLE `lunch` DISABLE KEYS */;
INSERT INTO `lunch` VALUES ('DOSA',120,'VEG'),('CURD RICE',100,'VEG'),('BIRYANI',150,'NON-VEG'),('MUTTON HANDI',300,'NON-VEG'),('JERA RICE',100,'VEG'),('RAJMA CHAWAL',120,'VEG'),('DAL MAKHANI',130,'VEG'),('PALAK PANEER',130,'VEG'),('PANEER BUTTER MASALA',150,'VEG'),('PANEER PULAO',130,'VEG'),('TANDOORI CHICKEN',130,'NON-VEG'),('BUTTER CHICKEN',140,'NON-VEG'),('CHILLI CHICKEN',145,'NON-VEG');
/*!40000 ALTER TABLE `lunch` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-04 16:17:04
