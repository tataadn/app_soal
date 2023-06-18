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
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
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
  `id_mapel` varchar(10) DEFAULT NULL,
  `id_kelas` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_mapel` (`id_mapel`),
  KEY `fk_kelas` (`id_kelas`),
  CONSTRAINT `fk_kelas` FOREIGN KEY (`id_kelas`) REFERENCES `tb_kelas` (`id_kelas`),
  CONSTRAINT `fk_mapel` FOREIGN KEY (`id_mapel`) REFERENCES `tb_mapel` (`id_mapel`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_user` */

insert  into `tb_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`,`nomor_induk`,`nama_lengkap`,`alamat`,`jenis_kelamin`,`is_siswa`,`is_guru`,`is_admin`,`foto`,`id_mapel`,`id_kelas`) values 
(1,'pbkdf2_sha256$600000$oY8bod4QeHkcMO88ED4hx7$97SHWJU/R7H9ph/bhwvk6RF886Z84GcxqpG1DJ6AJI0=','2023-06-18 13:17:04.007533',1,'adminsmp','','','smprahmat@gmail.com',1,1,'2023-06-05 14:23:22.000000','12345','Admin SMP','smp rahmat, bence','Perempuan',0,0,1,'foto/spongebob.jpg',NULL,NULL),
(2,'pbkdf2_sha256$600000$FuK1cXQYcR2XET6mg9B9cc$vAJsi3Pre0d1/yUwQbAfWuK6Ngw3cpqZNLyhXFQ+hnk=','2023-06-17 13:11:57.208871',0,'98765','','','anisaa@gmail.com',0,1,'2023-06-09 13:36:20.359857','98765','Anisa','ngadiluwih','Perempuan',0,1,0,'foto/teacher.jpg','MP03',NULL),
(3,'pbkdf2_sha256$600000$5twXCWSPYeN6p6ErFRJGBD$AyPa3nY2n+l+Sp4WfGYt7v8Av4o3F8GHywaMaNrwKag=','2023-06-10 17:06:41.545041',0,'23456','','','bumiahmad@gmail.com',0,1,'2023-06-09 13:52:08.638102','23456','Ahmad Bumi','gampengrejo, kediri','Laki-Laki',0,1,0,'foto/kim_bum.jpg','MP05',NULL),
(4,'pbkdf2_sha256$600000$0OW9crIOJBno77Da1S4HR0$ZIz6qeSZKiCdQHV43hjq4WpVe9VDWVlG9Awo/BrhzxQ=','2023-06-18 13:20:33.461438',0,'13579','','','sitiyuji@gmail.com',0,1,'2023-06-09 14:20:31.884422','13579','Siti Yuji','Sukorame, Kediri','Perempuan',1,0,0,'foto/ryujin.jpg',NULL,'7A'),
(5,'pbkdf2_sha256$600000$wj1MPUqGivKUOaHv65dFfc$tAHyDNsVppaNBQiddh29GZimRAkwkJd0Uqh6GrOZj4Q=','2023-06-18 13:20:13.395664',0,'123456789','','','dodiyanuar@gmail.com',0,1,'2023-06-18 13:19:42.936568','123456789','Dodi Yanuar','Kota Kediri','Laki-Laki',1,0,0,'foto/download.jpg',NULL,'7B');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
