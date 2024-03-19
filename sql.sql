/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - epharma
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`epharma` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `epharma`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add cart',7,'add_cart'),(20,'Can change cart',7,'change_cart'),(21,'Can delete cart',7,'delete_cart'),(22,'Can add feedback',8,'add_feedback'),(23,'Can change feedback',8,'change_feedback'),(24,'Can delete feedback',8,'delete_feedback'),(25,'Can add login',9,'add_login'),(26,'Can change login',9,'change_login'),(27,'Can delete login',9,'delete_login'),(28,'Can add medicine',10,'add_medicine'),(29,'Can change medicine',10,'change_medicine'),(30,'Can delete medicine',10,'delete_medicine'),(31,'Can add pharmacy',11,'add_pharmacy'),(32,'Can change pharmacy',11,'change_pharmacy'),(33,'Can delete pharmacy',11,'delete_pharmacy'),(34,'Can add purchase',12,'add_purchase'),(35,'Can change purchase',12,'change_purchase'),(36,'Can delete purchase',12,'delete_purchase'),(37,'Can add purchasehub',13,'add_purchasehub'),(38,'Can change purchasehub',13,'change_purchasehub'),(39,'Can delete purchasehub',13,'delete_purchasehub'),(40,'Can add rating',14,'add_rating'),(41,'Can change rating',14,'change_rating'),(42,'Can delete rating',14,'delete_rating'),(43,'Can add stock',15,'add_stock'),(44,'Can change stock',15,'change_stock'),(45,'Can delete stock',15,'delete_stock'),(46,'Can add user',16,'add_user'),(47,'Can change user',16,'change_user'),(48,'Can delete user',16,'delete_user');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'Epharma','cart'),(8,'Epharma','feedback'),(9,'Epharma','login'),(10,'Epharma','medicine'),(11,'Epharma','pharmacy'),(12,'Epharma','purchase'),(13,'Epharma','purchasehub'),(14,'Epharma','rating'),(15,'Epharma','stock'),(16,'Epharma','user'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'Epharma','0001_initial','2023-11-14 09:00:33.904744'),(2,'contenttypes','0001_initial','2023-11-14 09:00:34.007688'),(3,'auth','0001_initial','2023-11-14 09:00:35.191870'),(4,'admin','0001_initial','2023-11-14 09:00:35.509547'),(5,'admin','0002_logentry_remove_auto_add','2023-11-14 09:00:35.537513'),(6,'contenttypes','0002_remove_content_type_name','2023-11-14 09:00:35.794619'),(7,'auth','0002_alter_permission_name_max_length','2023-11-14 09:00:35.917331'),(8,'auth','0003_alter_user_email_max_length','2023-11-14 09:00:36.041188'),(9,'auth','0004_alter_user_username_opts','2023-11-14 09:00:36.070526'),(10,'auth','0005_alter_user_last_login_null','2023-11-14 09:00:36.183757'),(11,'auth','0006_require_contenttypes_0002','2023-11-14 09:00:36.193673'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-14 09:00:36.214844'),(13,'auth','0008_alter_user_username_max_length','2023-11-14 09:00:36.311382'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-14 09:00:36.403188'),(15,'sessions','0001_initial','2023-11-14 09:00:36.525720'),(16,'Epharma','0002_purchase_purchasehub','2023-12-13 08:44:17.323550'),(17,'Epharma','0003_purchase_status','2023-12-13 09:43:41.914121');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('icjiqwje7ce3idpp9tts9ity15vful12','NTZjMDY0ZWEyYTgzZDU2Mzg4MTcwMWVkNmQ4ODQ2MmE5NGRiMTMyZTp7InBpZCI6NSwibGlkIjo2fQ==','2023-12-27 10:45:15.464172');

/*Table structure for table `epharma_cart` */

DROP TABLE IF EXISTS `epharma_cart`;

CREATE TABLE `epharma_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(200) NOT NULL,
  `PHARMACY_id` int(11) NOT NULL,
  `STOCK_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_cart_PHARMACY_id_651fae84_fk_Epharma_pharmacy_id` (`PHARMACY_id`),
  KEY `Epharma_cart_STOCK_id_4e3eb9c9_fk_Epharma_stock_id` (`STOCK_id`),
  KEY `Epharma_cart_USER_id_2c8f33bf_fk_Epharma_user_id` (`USER_id`),
  CONSTRAINT `Epharma_cart_PHARMACY_id_651fae84_fk_Epharma_pharmacy_id` FOREIGN KEY (`PHARMACY_id`) REFERENCES `epharma_pharmacy` (`id`),
  CONSTRAINT `Epharma_cart_STOCK_id_4e3eb9c9_fk_Epharma_stock_id` FOREIGN KEY (`STOCK_id`) REFERENCES `epharma_stock` (`id`),
  CONSTRAINT `Epharma_cart_USER_id_2c8f33bf_fk_Epharma_user_id` FOREIGN KEY (`USER_id`) REFERENCES `epharma_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `epharma_cart` */

/*Table structure for table `epharma_feedback` */

DROP TABLE IF EXISTS `epharma_feedback`;

CREATE TABLE `epharma_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_feedback_USER_id_2e2ea049_fk_Epharma_user_id` (`USER_id`),
  CONSTRAINT `Epharma_feedback_USER_id_2e2ea049_fk_Epharma_user_id` FOREIGN KEY (`USER_id`) REFERENCES `epharma_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_feedback` */

insert  into `epharma_feedback`(`id`,`feedback`,`date`,`USER_id`) values (2,'ghgh','ghgjg',1);

/*Table structure for table `epharma_login` */

DROP TABLE IF EXISTS `epharma_login`;

CREATE TABLE `epharma_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_login` */

insert  into `epharma_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','4321','admin'),(2,'p','484854','pending'),(3,'p','484854','pending'),(4,'p','484854','pending'),(5,'p','1234','user'),(6,'p','123','pharmacy'),(7,'p','456','pharmacy'),(8,'deepuamardeep7@gmail.com','456','pharmacy'),(9,'deepuamardeep7@gmail.com','456','pharmacy'),(10,'alanbabyelickal@gmail.com','456','pharmacy'),(11,'deepuamardeep7@gmail.com','456','pharmacy'),(13,'alanbabyelickal@gmail.com','456','pharmacy'),(14,'deepuamardeep7@gmail.com','456','pharmacy'),(15,'deepuamardeep7@gmail.com','42423','pending'),(17,'alanbabyelickal@gmail.com','456','pharmacy'),(18,'alanbabyellickal@gmail.com','456','pharmacy'),(19,'safwankm456@gmail.com','456','pharmacy');

/*Table structure for table `epharma_medicine` */

DROP TABLE IF EXISTS `epharma_medicine`;

CREATE TABLE `epharma_medicine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_medicine` */

insert  into `epharma_medicine`(`id`,`name`) values (6,'shijinas'),(7,'sravan'),(8,'sharon'),(9,'jobit'),(10,'fgf');

/*Table structure for table `epharma_pharmacy` */

DROP TABLE IF EXISTS `epharma_pharmacy`;

CREATE TABLE `epharma_pharmacy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `latitude` varchar(200) NOT NULL,
  `longitude` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_pharmacy_LOGIN_id_8005bd9d_fk_Epharma_login_id` (`LOGIN_id`),
  CONSTRAINT `Epharma_pharmacy_LOGIN_id_8005bd9d_fk_Epharma_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `epharma_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_pharmacy` */

insert  into `epharma_pharmacy`(`id`,`name`,`email`,`phone`,`latitude`,`longitude`,`LOGIN_id`) values (5,'neethi','amal34@gmail.com',2434,'11.90985','75.71408',6),(6,'gdrgd','amal34@gmail.com',31879317,'2434','',7),(7,'afaf','deepuamardeep7@gmail',3124,'1234','',8),(8,'adsa','deepuamardeep7@gmail',21342,'324','',9),(9,'sfd','alanbabyelickal@gmai',65476,'6756856','',10),(10,'hgd','deepuamardeep7@gmail.com',31879317,'2434','',11),(13,'kjvgkiuy','deepuamardeep7@gmail.com',31879317,'2434','',14),(16,'jyhfjkvb','alanbabyelickal@gmail.com',45,'2434','',17),(17,'jfjh','alanbabyellickal@gmail.com',31879317,'2434','',18),(18,'uytuyhb','safwankm456@gmail.com',31879317,'2434','',19);

/*Table structure for table `epharma_purchase` */

DROP TABLE IF EXISTS `epharma_purchase`;

CREATE TABLE `epharma_purchase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `purchase` varchar(200) NOT NULL,
  `Delievery` varchar(200) NOT NULL,
  `latitude` varchar(200) NOT NULL,
  `longitude` varchar(200) NOT NULL,
  `PHARMACY_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `status` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_purchase_PHARMACY_id_4d31e25a_fk_Epharma_stock_id` (`PHARMACY_id`),
  KEY `Epharma_purchase_USER_id_daabfbae_fk_Epharma_user_id` (`USER_id`),
  CONSTRAINT `Epharma_purchase_PHARMACY_id_4d31e25a_fk_Epharma_stock_id` FOREIGN KEY (`PHARMACY_id`) REFERENCES `epharma_stock` (`id`),
  CONSTRAINT `Epharma_purchase_USER_id_daabfbae_fk_Epharma_user_id` FOREIGN KEY (`USER_id`) REFERENCES `epharma_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_purchase` */

insert  into `epharma_purchase`(`id`,`date`,`purchase`,`Delievery`,`latitude`,`longitude`,`PHARMACY_id`,`USER_id`,`status`) values (1,'55','55','yt','55','77',5,1,'rejected'),(2,'45','436','3445','53','543',5,1,'approved');

/*Table structure for table `epharma_purchasehub` */

DROP TABLE IF EXISTS `epharma_purchasehub`;

CREATE TABLE `epharma_purchasehub` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(200) NOT NULL,
  `PURCHASE_id` int(11) NOT NULL,
  `STOCK_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_purchasehub_PURCHASE_id_adbd4b42_fk_Epharma_purchase_id` (`PURCHASE_id`),
  KEY `Epharma_purchasehub_STOCK_id_712cccd5_fk_Epharma_stock_id` (`STOCK_id`),
  CONSTRAINT `Epharma_purchasehub_STOCK_id_712cccd5_fk_Epharma_stock_id` FOREIGN KEY (`STOCK_id`) REFERENCES `epharma_stock` (`id`),
  CONSTRAINT `Epharma_purchasehub_PURCHASE_id_adbd4b42_fk_Epharma_purchase_id` FOREIGN KEY (`PURCHASE_id`) REFERENCES `epharma_purchase` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_purchasehub` */

insert  into `epharma_purchasehub`(`id`,`quantity`,`PURCHASE_id`,`STOCK_id`) values (1,'44',1,1),(2,'22',1,3),(3,'43',1,5),(4,'49',1,2);

/*Table structure for table `epharma_rating` */

DROP TABLE IF EXISTS `epharma_rating`;

CREATE TABLE `epharma_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userrating` varchar(200) NOT NULL,
  `review` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `PHARMACY_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_rating_PHARMACY_id_047f5828_fk_Epharma_pharmacy_id` (`PHARMACY_id`),
  KEY `Epharma_rating_USER_id_3c0b0169_fk_Epharma_user_id` (`USER_id`),
  CONSTRAINT `Epharma_rating_PHARMACY_id_047f5828_fk_Epharma_pharmacy_id` FOREIGN KEY (`PHARMACY_id`) REFERENCES `epharma_pharmacy` (`id`),
  CONSTRAINT `Epharma_rating_USER_id_3c0b0169_fk_Epharma_user_id` FOREIGN KEY (`USER_id`) REFERENCES `epharma_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_rating` */

insert  into `epharma_rating`(`id`,`userrating`,`review`,`date`,`PHARMACY_id`,`USER_id`) values (4,'2','vhvch','4358',5,1);

/*Table structure for table `epharma_stock` */

DROP TABLE IF EXISTS `epharma_stock`;

CREATE TABLE `epharma_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(200) NOT NULL,
  `MEDICINE_id` int(11) NOT NULL,
  `PHARMACY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_stock_MEDICINE_id_e25b6df9_fk_Epharma_medicine_id` (`MEDICINE_id`),
  KEY `Epharma_stock_PHARMACY_id_b464f410_fk_Epharma_pharmacy_id` (`PHARMACY_id`),
  CONSTRAINT `Epharma_stock_MEDICINE_id_e25b6df9_fk_Epharma_medicine_id` FOREIGN KEY (`MEDICINE_id`) REFERENCES `epharma_medicine` (`id`),
  CONSTRAINT `Epharma_stock_PHARMACY_id_b464f410_fk_Epharma_pharmacy_id` FOREIGN KEY (`PHARMACY_id`) REFERENCES `epharma_pharmacy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_stock` */

insert  into `epharma_stock`(`id`,`quantity`,`MEDICINE_id`,`PHARMACY_id`) values (1,'42423',6,5),(2,'42423',7,5),(3,'42423',7,5),(5,'4321',8,5);

/*Table structure for table `epharma_user` */

DROP TABLE IF EXISTS `epharma_user`;

CREATE TABLE `epharma_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `Housename` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `post` varchar(200) NOT NULL,
  `pin` bigint(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Epharma_user_LOGIN_id_29cfc86c_fk_Epharma_login_id` (`LOGIN_id`),
  CONSTRAINT `Epharma_user_LOGIN_id_29cfc86c_fk_Epharma_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `epharma_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `epharma_user` */

insert  into `epharma_user`(`id`,`name`,`phone`,`Housename`,`place`,`post`,`pin`,`email`,`LOGIN_id`) values (1,'dfd',54545,'hvh','hvbvh','jbjh',777,'ghgghh',5);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
