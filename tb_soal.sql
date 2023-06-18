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
  `id_kelas` varchar(10) NOT NULL,
  `id_mapel` varchar(10) NOT NULL,
  `kode_soal` varchar(50) NOT NULL,
  `soal` longtext NOT NULL,
  `kunci_jawaban` longtext NOT NULL,
  `bobot_soal` int(11) NOT NULL,
  `id_user` bigint(20) NOT NULL,
  PRIMARY KEY (`id_soal`),
  KEY `fk_user` (`id_user`),
  CONSTRAINT `fk_user` FOREIGN KEY (`id_user`) REFERENCES `tb_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tb_soal` */

insert  into `tb_soal`(`id_soal`,`id_kelas`,`id_mapel`,`kode_soal`,`soal`,`kunci_jawaban`,`bobot_soal`,`id_user`) values 
(1,'7A','MP03','KDS001','Sebutkan ciri ciri yang ada pada kalimat tidak langsung!','Tidak memakai tanda petik pada kalimat, cara membacanya tidak dengan ekspresi atau datar dan adanya pada pemakaian kata ganti orang.',20,2),
(2,'7A','MP03','KDS001','Sebutkan apa saja ciri-ciri pantun!','Memiliki empat baris di tiap bait, jumlah suku kata 8 sampai 12 di tiap baris, dengan memiliki rima akhir a-b-a-b. Sampiran di baris pertama dan kedua dan Isi terdapat di baris ketiga dan keempat.',20,2),
(3,'7A','MP03','KDS001','pengertian dari rima?','Pengulangan kata pada sajak baik di awal maupun di akhir',20,2),
(4,'7A','MP03','KDS001','Yang merupakan pengarang syair berjudul ‘Syair Perahu’ adalah','Hamzah Fansuri',20,2),
(6,'7A','MP03','KDS001','Gurindam merupakan puisi lama dari bahasa India yaitu kirindam yang artinya?','Mula-mula atau perumpamaan',20,2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
