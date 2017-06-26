/*
Navicat MySQL Data Transfer

Source Server         : db
Source Server Version : 50718
Source Host           : 127.0.0.1:3306
Source Database       : minghe

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-06-26 12:32:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gzh
-- ----------------------------
DROP TABLE IF EXISTS `gzh`;
CREATE TABLE `gzh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `created_at` varchar(255) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `auth` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
