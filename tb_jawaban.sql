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

/*Table structure for table `tb_jawaban` */

DROP TABLE IF EXISTS `tb_jawaban`;

CREATE TABLE `tb_jawaban` (
  `id_jawaban` int(11) NOT NULL AUTO_INCREMENT,
  `id_soal` int(11) NOT NULL,
  `jawaban_siswa` text NOT NULL,
  `nilai` double NOT NULL,
  `id_siswa` bigint(20) NOT NULL,
  `tgl_ujian` datetime(6) NOT NULL,
  PRIMARY KEY (`id_jawaban`),
  KEY `fk_idsoal` (`id_soal`),
  KEY `fk_idsiswa` (`id_siswa`),
  CONSTRAINT `fk_soal` FOREIGN KEY (`id_soal`) REFERENCES `tb_soal` (`id_soal`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_jawaban` */

insert  into `tb_jawaban`(`id_jawaban`,`id_soal`,`jawaban_siswa`,`nilai`,`id_siswa`,`tgl_ujian`) values 
(1,1,'Tidak menggunakan tanda petik pada kalimat\r\nCara membacanya atau nadanya datar\r\nAdanya perubahan kata ganti orang',19,18,'2023-07-06 15:29:43.167945'),
(2,2,'Terdapat empat baris pada tiap bait\r\nJumlah suku kata sekitar 8 sampai 12 suku kata pada tiap baris\r\nSetiap baris memiliki rima akhir a-b-a-b',14,18,'2023-07-06 15:29:43.168945'),
(3,3,'Dalam satu bait terdiri dari dua baris\r\nJumlah kata pada tiap baris sekitar 10 sampai 14 kata\r\nRima pada tiap baris bersajak a-a, b-b, c-c, dan seterusnya',12,18,'2023-07-06 15:29:43.169946'),
(4,4,'Tokoh; binatang menjadi pelaku dalam cerita baik tokoh protagonis maupun antagonis, tokoh utama (sering dibicarakan, sering muncul) atau pembantu (tambahan)\r\nPenokohan dan watak tokoh; tokoh diberikan karakter atau sifat\r\nsetting, tema, amanat',15,18,'2023-07-06 15:29:43.170945'),
(5,5,'Gedong gincu diresmikan sebagai salah 1 simbol Indramayu. Peresmiannya dilakukan oleh Ibu Hj. Ana Sophana pada puncak peringatan hari jadi Indramayu yang ke-491 tanggal 7 Oktober 2018.',19,18,'2023-07-06 15:29:43.172943'),
(6,1,'Tidak menggunakan tanda petik pada kalimat\r\nCara membacanya atau nadanya datar\r\nAdanya perubahan kata ganti orang',19,20,'2023-07-06 15:37:09.015939'),
(7,2,'Setiap baris memiliki rima akhir a-b-a-b\r\nSampiran terdapat pada baris pertama dan kedua\r\nIsi terdapat pada baris ketiga dan keempat',14,20,'2023-07-06 15:37:09.016938'),
(8,3,'Soal, masalah, atau perjanjian terdapat pada baris pertama\r\nJawaban atau akibat terdapat pada baris kedua\r\nBerisi tentang nasihat, kata-kata mutiara atau filosofi hidup',13,20,'2023-07-06 15:37:09.016938'),
(9,4,'Penokohan dan watak tokoh; tokoh diberikan karakter atau sifat\r\nSetting/latar; tempat, waktu, sosial pada cerita\r\nTema; ide atau gagasan yang mendasari cerita\r\nAmanat; pesan cerita tersebut',3,20,'2023-07-06 15:37:09.017940'),
(10,5,'Gedong Gincu diresmikan sebagai salah satu symbol Indramayu. Peresmiannya dilakukan oleh Ibu Hj. Ana Sophana pada puncak peringatan hari jadi Indramayu yang ke-491 tanggal 7 Oktober 2018.',20,20,'2023-07-06 15:37:09.018942');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
