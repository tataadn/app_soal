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

/*Table structure for table `tb_user` */

DROP TABLE IF EXISTS `tb_user`;

CREATE TABLE `tb_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nomor_induk` varchar(200) NOT NULL,
  `nama_lengkap` varchar(255) NOT NULL,
  `alamat` longtext NOT NULL,
  `jenis_kelamin` varchar(10) NOT NULL,
  `is_siswa` tinyint(1) NOT NULL,
  `is_guru` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `id_mapel` varchar(50) DEFAULT NULL,
  `id_kelas` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_mapel` (`id_mapel`),
  KEY `fk_kelas` (`id_kelas`),
  CONSTRAINT `fk_kelas` FOREIGN KEY (`id_kelas`) REFERENCES `tb_kelas` (`id_kelas`),
  CONSTRAINT `fk_mapel` FOREIGN KEY (`id_mapel`) REFERENCES `tb_mapel` (`id_mapel`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_user` */

insert  into `tb_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`nomor_induk`,`nama_lengkap`,`alamat`,`jenis_kelamin`,`is_siswa`,`is_guru`,`is_admin`,`foto`,`id_mapel`,`id_kelas`) values 
(1,'pbkdf2_sha256$180000$gmLmJM9h4vRP$+Yrze8MqCx9gimFQEEQC61FPw+MVnLBxO8Es/or0uQI=','2023-07-06 15:38:21.040430',1,'adminsmp','','','Info@rahmat.sch.id',1,1,'2023-06-05 14:23:22.000000','12345','Admin SMP','Jl. Kapten Tendean, Bence Gg.I, Pakunden – Kota Kediri','Perempuan',0,0,1,'foto/LOGO_BARU.png',NULL,NULL),
(6,'pbkdf2_sha256$600000$4WB2IucgilOmsOgXiKqJSf$/8b89EYje0/dZiBu6EfY0rpXT/e9uQzXaT7Jd9Ty+ck=',NULL,0,'123456789','','','dhaninjaya@gmail.com',0,1,'2023-06-21 10:29:37.002422','123456789','Deehan Dhaninjaya','Kota Kediri','Laki-Laki',1,0,0,'foto/download_UkxWM1Y.jpg',NULL,'7B'),
(15,'pbkdf2_sha256$180000$LiU4Jqz9MjL0$kGaOb7uND34hWMvUBjUrArWbgCnQQBhWVqZwKVQuW8Q=',NULL,0,'20190221','','','subandiyantoro@gmail.com',0,1,'2023-07-06 14:25:21.429652','20190221','Subandiyantoro, S.Pd., M.Pd','Ngadiluwih, Kediri','Laki-Laki',0,1,0,'foto/photo_6140787057358911304_y.jpg','MP03',NULL),
(16,'pbkdf2_sha256$180000$fx49gFYPPdIe$ywqQfzvB0eTjhPDjTewOMN5HAuYN6NQXpNXkCYs7e/g=','2023-07-06 15:37:49.748394',0,'20171121','','','hajarsholeha@gmail.com',0,1,'2023-07-06 14:26:09.865659','20171121','Hajar Solehah, S.Pd','Gampengrejo, Kediri','Perempuan',0,1,0,'foto/photo_6140787057358911305_y.jpg','MP02',NULL),
(17,'pbkdf2_sha256$180000$bVDCCBucNWYe$FOqONa+SYbWSfXFGWjWb152x4P3EQy/nA/fB9+yWlsM=','2023-07-06 15:38:38.467321',0,'20170302','','','humaidah23@gmail.com',0,1,'2023-07-06 14:28:16.509658','20170302','Indah Humaidah, S.Hum','Kota Kediri','Perempuan',0,1,0,'foto/photo_6140787057358911306_y.jpg','MP01',NULL),
(18,'pbkdf2_sha256$180000$hR5zP7k2lKSN$08kFmbseyXD/5cKVT314cJ8gCgDhDr+X/gwSwNrUszQ=','2023-07-06 15:27:20.646893',0,'0099876804','','','iqlima.hani@gmail.com',0,1,'2023-07-06 14:36:31.965378','0099876804','Iqlima Ainun Hanifah','Gampengrejo, Kediri','Perempuan',1,0,0,'foto/Iqlima_Ainun_Hanifah.jpeg',NULL,'7A'),
(19,'pbkdf2_sha256$180000$RLRNr8yYMRfl$YXsbPb7yiPPY87I0UJrjBi6oZXVBp1VHRGf/PuZlDIE=',NULL,0,'0098852841','','','sirinabidah@gmail.com',0,1,'2023-07-06 14:38:51.217636','0098852841','Sirin Abidah','Kota Kediri','Perempuan',1,0,0,'foto/Sirin_Abidah.jpeg',NULL,'7A'),
(20,'pbkdf2_sha256$180000$nl4WlyaucJvz$1lloxyoU0cK568JG+4Ra7xVoDaebyMAQAIyHWFzSUgE=','2023-07-06 15:35:44.886222',0,'0097816504','','','permataaura@gmail.com',0,1,'2023-07-06 14:39:40.715526','0097816504','Permata Aura','Kota Kediri','Perempuan',1,0,0,'foto/Permata_Aura.jpeg',NULL,'7A');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
