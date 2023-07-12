/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 10.4.28-MariaDB : Database - db_smp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_smp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `db_smp`;

/*Table structure for table `tb_kdsoal` */

DROP TABLE IF EXISTS `tb_kdsoal`;

CREATE TABLE `tb_kdsoal` (
  `id_kdsoal` int(11) NOT NULL AUTO_INCREMENT,
  `kode_soal` varchar(50) NOT NULL,
  `nama_ujian` varchar(255) NOT NULL,
  `jumlah_soal` int(11) NOT NULL,
  `id_mapel` varchar(50) NOT NULL,
  `id_kelas` varchar(50) NOT NULL,
  `id_user` int(11) NOT NULL,
  `tgl_input` datetime(6) NOT NULL,
  PRIMARY KEY (`id_kdsoal`),
  KEY `fk_mpl` (`id_mapel`),
  KEY `fk_user` (`id_user`),
  KEY `fk_kls` (`id_kelas`),
  CONSTRAINT `fk_mpl` FOREIGN KEY (`id_mapel`) REFERENCES `tb_mapel` (`id_mapel`),
  CONSTRAINT `fk_user` FOREIGN KEY (`id_user`) REFERENCES `tb_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_kdsoal` */

insert  into `tb_kdsoal`(`id_kdsoal`,`kode_soal`,`nama_ujian`,`jumlah_soal`,`id_mapel`,`id_kelas`,`id_user`,`tgl_input`) values 
(1,'KDS001','Ulangan Bhs Inggris Bab 1',5,'MP02','7A',16,'2023-07-06 14:51:32.857652'),
(2,'KDS002','Ulangan Bhs Indo Bab 1',5,'MP01','7A',17,'2023-07-06 15:04:01.023556');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
