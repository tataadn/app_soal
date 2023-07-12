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

/*Table structure for table `tb_soal` */

DROP TABLE IF EXISTS `tb_soal`;

CREATE TABLE `tb_soal` (
  `id_soal` int(11) NOT NULL AUTO_INCREMENT,
  `id_kdsoal` int(11) NOT NULL,
  `soal` longtext NOT NULL,
  `kunci_jawaban` longtext NOT NULL,
  `bobot_soal` int(11) NOT NULL,
  `tgl_input` datetime DEFAULT NULL,
  PRIMARY KEY (`id_soal`),
  KEY `fk_kdsoal` (`id_kdsoal`),
  CONSTRAINT `fk_kdsoal` FOREIGN KEY (`id_kdsoal`) REFERENCES `tb_kdsoal` (`id_kdsoal`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_soal` */

insert  into `tb_soal`(`id_soal`,`id_kdsoal`,`soal`,`kunci_jawaban`,`bobot_soal`,`tgl_input`) values 
(1,2,'Sebutkan apa saja ciri-ciri kalimat tidak langsung!','- Tidak menggunakan tanda petik pada kalimat\r\n- Cara membacanya atau nadanya datar\r\n- Adanya perubahan kata ganti orang',20,'2023-07-06 15:07:48'),
(2,2,'Sebutkan apa saja ciri-ciri pantun!','- Terdapat empat baris pada tiap bait\r\n- Jumlah suku kata sekitar 8 sampai 12 suku kata pada tiap baris\r\n- Setiap baris memiliki rima akhir a-b-a-b\r\n- Sampiran terdapat pada baris pertama dan kedua\r\n- Isi terdapat pada baris ketiga dan keempat',20,'2023-07-06 15:22:53'),
(3,2,'Sebutkan apa saja ciri-ciri gurindam!','- Dalam satu bait terdiri dari dua baris\r\n- Jumlah kata pada tiap baris sekitar 10 sampai 14 kata\r\n- Rima pada tiap baris bersajak a-a, b-b, c-c, dan seterusnya\r\n- Soal, masalah, atau perjanjian terdapat pada baris pertama\r\n- Jawaban atau akibat terdapat pada baris kedua\r\n- Berisi tentang nasihat, kata-kata mutiara atau filosofi hidup',20,'2023-07-06 15:23:49'),
(4,2,'Sebutkan unsur-unsur yang terdapat pada Fabel dan jelaskan!','- Tokoh; binatang menjadi pelaku dalam cerita baik tokoh protagonis maupun antagonis, tokoh utama (sering dibicarakan, sering muncul) atau pembantu (tambahan)\r\n- Penokohan dan watak tokoh; tokoh diberikan karakter atau sifat\r\n- Setting/latar; tempat, waktu, sosial pada cerita\r\n- Tema; ide atau gagasan yang mendasari cerita\r\n- Amanat; pesan cerita tersebut',20,'2023-07-06 15:25:02'),
(5,2,'Perbaikilah penggunaan huruf kapital pada teks berikut!\r\n\r\ngedong gincu diresmikan sebagai salah satu simbol indramayu. Peresmiannya dilakukan oleh ibu hj. anasophana pada puncak peringatan hari jadi indramayu yang ke-491, tanggal 7 oktober 2018.','Gedong Gincu diresmikan sebagai salah satu symbol Indramayu. Peresmiannya dilakukan oleh Ibu Hj. Ana Sophana pada puncak peringatan hari jadi Indramayu yang ke-491 tanggal 7 Oktober 2018.',20,'2023-07-06 15:26:04');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
