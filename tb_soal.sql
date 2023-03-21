/*
SQLyog Ultimate
MySQL - 10.4.22-MariaDB : Database - smpplusrahmat
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smpplusrahmat` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `smpplusrahmat`;

/*Table structure for table `tb_soal` */

DROP TABLE IF EXISTS `tb_soal`;

CREATE TABLE `tb_soal` (
  `id_soal` int(10) NOT NULL AUTO_INCREMENT,
  `id_kelas` varchar(10) NOT NULL,
  `id_mapel` varchar(10) NOT NULL,
  `soal` text NOT NULL,
  `kunci_jawaban` text NOT NULL,
  PRIMARY KEY (`id_soal`),
  KEY `fkkelas` (`id_kelas`),
  KEY `fkmapel` (`id_mapel`),
  CONSTRAINT `fkkelas` FOREIGN KEY (`id_kelas`) REFERENCES `tb_kelas` (`id_kelas`),
  CONSTRAINT `fkmapel` FOREIGN KEY (`id_mapel`) REFERENCES `tb_mapel` (`id_mapel`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_soal` */

insert  into `tb_soal`(`id_soal`,`id_kelas`,`id_mapel`,`soal`,`kunci_jawaban`) values (1,'7A','BINDO','Jelaskan pengertian dari cerpen!','Cerpen merupakan suatu karya sastra dalam bentuk tulisan yang mengisahkan tentang sebuah cerita fiksi lalu dikemas secara pendek, jelas dan ringkas.'),(2,'7A','BINDO','Apa itu Koda dalam struktur cerpen? Jelaskan!','Koda merupakan nilai atau pesan moral yang terdapat pada sebuah cerpen yang disampaikan oleh penulis kepada para pembaca. Pesan moral yang disampaikan sesuai dengan jenis cerpen.');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
