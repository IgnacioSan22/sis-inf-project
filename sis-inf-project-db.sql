-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2018 at 07:59 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sis-inf-project-db`
--

-- --------------------------------------------------------

--
-- Table structure for table `posters`
--

CREATE TABLE `posters` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `imagen` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `titulo` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `reto` varchar(2048) COLLATE utf8_unicode_ci DEFAULT NULL,
  `info` varchar(2048) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pregunta` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `respuesta_correcta` int(11) DEFAULT NULL,
  `corregido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `posters`
--

INSERT INTO `posters` (`id`, `id_usuario`, `imagen`, `titulo`, `reto`, `info`, `pregunta`, `respuesta_correcta`, `corregido`) VALUES
(5, 15, 'http://www.imagen.com.mx/assets/img/imagen_share.png', 'Titulo Poster 1', 'Nulla facilisi. Donec ut vulputate ante. Cras pretium fermentum sem, vitae finibus enim cursus sit amet. Mauris ornare mi nec mi euismod aliquet vel quis lorem. Aliquam porta quam tellus, sed pellentesque massa varius ac. Nunc lectus mauris, ultrices et mi nec, egestas pharetra nisi. Etiam a tristique nisi. Mauris eget mi quis ante pulvinar pretium. ', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam faucibus nisl nec eros ornare, eu tempus orci finibus. Morbi ut ornare ex. Aenean consectetur, eros eu condimentum tristique, enim urna venenatis arcu, id elementum sapien dui fermentum nibh. Sed dui felis, porta et metus sit amet, tempor faucibus velit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum maximus, justo convallis tincidunt rutrum, ligula ligula condimentum dolor, eu ornare orci dolor nec nisl. Morbi lacus nulla, molestie eget pellentesque pretium, tempus sed massa. Quisque efficitur tortor a neque viverra lacinia. Morbi congue, lectus tincidunt pulvinar vestibulum, leo mauris eleifend metus, eget faucibus mauris urna id augue. \r\n\r\nInteger ac massa placerat, laoreet orci et, pellentesque lorem. Integer vitae velit et justo bibendum sodales at in nisi. Cras sodales volutpat dui, non vehicula odio porta id. Cras est ex, faucibus quis nibh eu, lacinia placerat tellus. Praesent consequat tortor nec feugiat finibus. Cras tellus velit, finibus et imperdiet sed, accumsan in mauris. Nulla eleifend et arcu vitae pulvinar. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque vitae euismod orci. Donec vitae justo a eros hendrerit viverra. Morbi finibus consequat tincidunt. Aliquam erat volutpat. Vestibulum et nibh purus. Pellentesque accumsan sapien eu fermentum feugiat. Morbi efficitur enim ut odio ornare, sit amet molestie tortor luctus. Aliquam a massa at tellus consequat euismod ut tempor turpis. ', '¿Lorem ipsum dolor sit amet?', NULL, 1),
(6, 15, 'https://d2jljza7x0a5yy.cloudfront.net/media/k2/items/cache/ef1967223c9adfad3d0bc3925439651e_XL.jpg?t=1464157377', 'Titulo Poster 2', 'Sed pharetra ligula ut ultrices lacinia. Etiam eget posuere nisl. Integer lectus odio, lacinia ac vehicula eget, cursus at sapien. Nullam vitae dolor aliquet, gravida ligula a, gravida enim. Etiam malesuada semper urna sed tristique. Cras ut congue metus, non ullamcorper risus. Vestibulum ultrices dignissim tristique. Maecenas molestie purus non metus rhoncus sollicitudin. Ut vitae urna interdum, ornare velit eu, elementum odio. Cras tincidunt lectus purus, ac aliquet nibh consectetur ornare. Donec diam mauris, imperdiet eget dolor a, pulvinar rutrum ex. Vivamus vitae tristique orci. Aenean feugiat mauris sit amet suscipit accumsan. Vestibulum tincidunt, turpis quis pretium venenatis, nisl nisl pharetra sem, sit amet scelerisque elit arcu vitae tortor. ', 'Nunc tellus magna, laoreet at consequat ut, mattis in nulla. Maecenas ultrices purus mi, ac tincidunt sapien dictum ut. In tincidunt magna eu erat ultricies iaculis. Nunc vitae rutrum urna. Donec ultricies diam at laoreet tempor. Morbi non tellus euismod, varius turpis sit amet, maximus neque. Duis ultrices nisl vel odio rhoncus pharetra. In finibus mollis semper. Donec viverra magna mi, eget auctor lectus porttitor non. Fusce maximus semper venenatis. Aliquam urna augue, eleifend placerat neque ut, maximus volutpat mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut posuere maximus neque, sit amet hendrerit dui fringilla sit amet. Praesent bibendum lectus ut sagittis elementum. Vestibulum eu orci quis justo consequat interdum. Praesent mattis ex vel augue auctor, ut dapibus nisi interdum. ', '¿Dolor si amet lorem ipsum?', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `preguntas`
--

CREATE TABLE `preguntas` (
  `id` int(11) NOT NULL,
  `pregunta` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,
  `year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `question_options`
--

CREATE TABLE `question_options` (
  `id` int(11) NOT NULL,
  `id_poster` int(11) DEFAULT NULL,
  `opcion` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
  `correcta` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `question_options`
--

INSERT INTO `question_options` (`id`, `id_poster`, `opcion`, `correcta`) VALUES
(17, 5, 'Dolor', NULL),
(18, 5, 'Lorem', NULL),
(19, 5, 'Ipsum', NULL),
(20, 5, 'Sit amet', NULL),
(21, 6, 'Lorem', NULL),
(22, 6, 'Ipsum', NULL),
(23, 6, 'Dolor', NULL),
(24, 6, 'Sit amet', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `question_options_2`
--

CREATE TABLE `question_options_2` (
  `id` int(11) NOT NULL,
  `id_pregunta` int(11) DEFAULT NULL,
  `opcion` varchar(512) COLLATE utf8_unicode_ci DEFAULT NULL,
  `correcta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stats`
--

CREATE TABLE `stats` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `dato_estadistico_1` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dato_estadistico_2` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dato_estadistico_3` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `stats`
--

INSERT INTO `stats` (`id`, `id_usuario`, `dato_estadistico_1`, `dato_estadistico_2`, `dato_estadistico_3`) VALUES
(1, 1, 'B', '19-22', 'H'),
(2, NULL, 'B', '19-22', 'H'),
(3, NULL, 'U', '0-18', 'M'),
(4, NULL, 'A', '+22', 'M'),
(5, NULL, 'U', '0-18', 'M');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nombre` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apellidos` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nia` varchar(6) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password_hash` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipo_usuario` int(11) DEFAULT NULL,
  `validated` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `nombre`, `apellidos`, `nia`, `email`, `password_hash`, `tipo_usuario`, `validated`) VALUES
(1, 'victor', NULL, NULL, NULL, 'melic93@gmail.com', 'pbkdf2:sha256:50000$59vzEpej$4a30b26885038a572a213173503d7a1afc8472a54bdfc66368dbc51cb5f76df8', 1, 1),
(2, 'eduardo', NULL, NULL, NULL, 'edumoreno@gmail.com', 'pbkdf2:sha256:50000$iAdT6cR5$4a56000bf186848c37a2ae17cdeb3291b8be0bfd2ef4b55c4cde48497d0f086e', 2, 1),
(3, 'ignacio', NULL, NULL, NULL, 'ignacio@gmail.com', 'pbkdf2:sha256:50000$RenEVb24$602d73d4cc4a0d75d3f4c89d60be68c32735aea9fa4e557451dab38162e31784', 2, 1),
(4, 'eduvalido', NULL, NULL, NULL, 'eduvalido@gmail.com', 'pbkdf2:sha256:50000$vbDSsy1f$98f85cc72f7389377ff4ffa662c3df1ef087cad9765a8303d61db7b0d98cc37a', 2, 1),
(6, 'valido', NULL, NULL, NULL, 'valido@gmail.com', 'pbkdf2:sha256:50000$NCVbSBjd$4567fbcc911ee7abc31c2fb0c552c3f6ac2f68185122c32b06772456056acfab', 2, 1),
(7, 'invalido', NULL, NULL, NULL, 'invalido@unizar.es', 'pbkdf2:sha256:50000$zpeJbGZW$23b380c38ee36b03020fa97e221cae400648ed9d407bfdca5b9e12a4bbd90db2', 2, 1),
(8, 'invalido2', NULL, NULL, NULL, 'invalido2@gmail.com', 'pbkdf2:sha256:50000$r4NxoZJm$98713d9fd7cdcd10f37241b056078c98068e3ba0506222637a348bd12505e8f9', 2, 1),
(10, 'melic', NULL, NULL, NULL, 'vfmelic@unizar.es', 'pbkdf2:sha256:50000$GXG5tU49$ea3afb65a606078d89e128410527bb037577978ec0891d6e74cc4a88262a936b', 2, 1),
(11, 'prueba', NULL, NULL, NULL, 'usuario@a.es', 'pbkdf2:sha256:50000$bkr8yWNV$32934b8fe72d6b4b2a2e7713438bb4e809fcff4169c09d26328912f135d1e506', 2, 1),
(12, 'hola', NULL, NULL, NULL, 'hola@mail.es', 'pbkdf2:sha256:50000$32sG2IX3$8461688efc365b2de299631f2623cbf62c876b6b6a6cac36fd4afdb708c38ceb', 2, 1),
(13, 'JorgeGG', 'Jorge', 'Generelo Gimeno', '737317', '737317@unizar.es', 'pbkdf2:sha256:50000$ZUpurfpq$9ffeb3891c526af8c1cc584fba200ed8e39e27ddb571983907c2666d47544c03', 2, 1),
(14, 'lalala', 'lalala', 'lalala', '765412', 'lalala@sdfsdf.es', 'pbkdf2:sha256:50000$PreuZtns$e3c82396fdccb9bde015ac600339a83ebf147e6cd5a5154952ad668336eb5961', 2, 1),
(15, 'rosario', 'Rosario', 'Lissandrello', '123456', 'rlissa@unizar.es', 'pbkdf2:sha256:50000$vN2kwW7O$32b9761f3a73dd248249905bf1dc5e64f303a94f7b930ef15f2c8dc2116d546c', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_likes`
--

CREATE TABLE `user_likes` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_poster` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user_likes`
--

INSERT INTO `user_likes` (`id`, `id_usuario`, `id_poster`) VALUES
(1, 1, 3),
(2, 15, 5);

-- --------------------------------------------------------

--
-- Table structure for table `user_response`
--

CREATE TABLE `user_response` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_poster` int(11) DEFAULT NULL,
  `opcion` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user_response`
--

INSERT INTO `user_response` (`id`, `id_usuario`, `id_poster`, `opcion`) VALUES
(1, 15, 5, 'Dolor'),
(2, 15, 5, 'Sit amet'),
(3, 15, 5, 'Dolor'),
(4, 15, 5, 'Ipsum'),
(5, 15, 5, 'Sit amet');

-- --------------------------------------------------------

--
-- Table structure for table `user_response2`
--

CREATE TABLE `user_response2` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_opcion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posters`
--
ALTER TABLE `posters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `preguntas`
--
ALTER TABLE `preguntas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `question_options`
--
ALTER TABLE `question_options`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `question_options_2`
--
ALTER TABLE `question_options_2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pregunta` (`id_pregunta`);

--
-- Indexes for table `stats`
--
ALTER TABLE `stats`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_email` (`email`),
  ADD UNIQUE KEY `ix_users_username` (`username`),
  ADD UNIQUE KEY `nia_index` (`nia`) USING BTREE;

--
-- Indexes for table `user_likes`
--
ALTER TABLE `user_likes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `user_response`
--
ALTER TABLE `user_response`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `user_response2`
--
ALTER TABLE `user_response2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_opcion` (`id_opcion`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `posters`
--
ALTER TABLE `posters`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `preguntas`
--
ALTER TABLE `preguntas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `question_options`
--
ALTER TABLE `question_options`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `question_options_2`
--
ALTER TABLE `question_options_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stats`
--
ALTER TABLE `stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `user_likes`
--
ALTER TABLE `user_likes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_response`
--
ALTER TABLE `user_response`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_response2`
--
ALTER TABLE `user_response2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `posters`
--
ALTER TABLE `posters`
  ADD CONSTRAINT `posters_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `users` (`id`);

--
-- Constraints for table `question_options_2`
--
ALTER TABLE `question_options_2`
  ADD CONSTRAINT `question_options_2_ibfk_1` FOREIGN KEY (`id_pregunta`) REFERENCES `preguntas` (`id`);

--
-- Constraints for table `user_likes`
--
ALTER TABLE `user_likes`
  ADD CONSTRAINT `user_likes_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_response`
--
ALTER TABLE `user_response`
  ADD CONSTRAINT `user_response_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_response2`
--
ALTER TABLE `user_response2`
  ADD CONSTRAINT `user_response2_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `user_response2_ibfk_2` FOREIGN KEY (`id_opcion`) REFERENCES `question_options_2` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
