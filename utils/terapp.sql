-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-12-2022 a las 06:59:56
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `terapp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agenda`
--

CREATE TABLE `agenda` (
  `id` int(11) NOT NULL,
  `nombre_apellido` varchar(40) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `observaciones` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `agenda`
--

INSERT INTO `agenda` (`id`, `nombre_apellido`, `fecha`, `hora`, `observaciones`) VALUES
(2, 'Luis Perez', '2022-12-11', '00:00:00', ''),
(3, 'Lucas Bustos', '2022-11-01', '00:00:00', ''),
(4, 'Luis Perez', '2022-05-05', '00:00:00', ''),
(5, 'Romina Pringles', '2023-11-15', '00:00:00', ''),
(6, 'Romina Lopez', '2023-10-11', '00:00:00', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactenos`
--

CREATE TABLE `contactenos` (
  `id` int(20) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  `asunto` varchar(255) NOT NULL,
  `mensaje` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `contactenos`
--

INSERT INTO `contactenos` (`id`, `nombre`, `email`, `telefono`, `asunto`, `mensaje`) VALUES
(1, 'Agustina', 'agustina_hidalgo@outlook.com', '123456', 'Consulta', 'hlñfglhfgklhfgñhñlgfkhlfgñhfg'),
(7, 'Teresa', 'teresa.test@gmail.com', '7845221', 'Consulta', 'jkfdslkjdskljdskjfmcmx fkks losdfsdkfds jsdofksdkfñlskd jlsdfdskfñsdñkf skfñskñdf'),
(8, 'Marcos', 'marcos@mail.com', '12345678', 'importante', 'asunto importante a tratar'),
(9, 'Nora', 'nora@mail.com', '88888888', 'Asunto', 'msg'),
(12, 'Flash', 'flash@gordon.con', '00000', 'Otro', 'Problemas en formulario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obra_social`
--

CREATE TABLE `obra_social` (
  `id_obra_social` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `obra_social`
--

INSERT INTO `obra_social` (`id_obra_social`, `nombre`) VALUES
(1, 'No aplica / paciente particular'),
(2, 'Swiss Medical'),
(3, 'Galeno'),
(4, 'Medicus'),
(5, 'Osseg'),
(6, 'Opdea'),
(7, 'Elevar'),
(8, 'Osde'),
(9, 'SanCor Salud'),
(10, 'Hominis'),
(11, 'Osdipp'),
(12, 'Ospic');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `edad` int(11) NOT NULL,
  `tutor` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_obra_social` int(11) NOT NULL,
  `n_afiliado` int(11) NOT NULL,
  `dni` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `diagnostico` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_de_nacimiento` date NOT NULL,
  `fecha_de_ingreso` date NOT NULL,
  `observaciones` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`id`, `nombre`, `apellido`, `edad`, `tutor`, `id_obra_social`, `n_afiliado`, `dni`, `email`, `telefono`, `domicilio`, `diagnostico`, `fecha_de_nacimiento`, `fecha_de_ingreso`, `observaciones`) VALUES
(34, 'Nora', 'Barria', 20, '-', 1, 1245648, 36645898, 'nora.barria@gmail.com', 48702654, 'Nueva York 123', '-', '1990-05-08', '2021-02-12', '-'),
(35, 'Marcos', 'Gutierrez', 24, '-', 1, 2147483647, 12345678, 'marcos.gutierrez@hotmail.com', 1557263899, 'Bahia Blanca 2620', '-', '1997-07-03', '2021-11-01', '-'),
(36, 'Gonzalo', 'Galarza', 28, 'Nora Barria', 2, 21888456, 35000856, 'gonzalo.galarza@yahoo.com', 48705698, 'Lascano 123', '-', '1993-11-10', '2021-11-10', '-'),
(37, 'Maria', 'Eizayaga', 26, '-', 3, 541567893, 38589753, 'maria.eizayaga@outlook.com', 1587963255, 'Concordia 2587', '-', '1995-11-11', '2021-11-16', '-'),
(38, 'Francisco', 'Ceccoli', 47, '-', 4, 123501264, 20123582, 'francisco.ceccoli@msn.com', 45896235, 'Sanabria 789', '-', '1975-01-01', '2021-11-01', '-'),
(39, 'Lidia', 'Medina', 51, '-', 5, 1, 11263324, 'medinalidia3@gmail.com', 42058978, 'Nazarre 3487', '-', '1960-06-02', '2021-11-01', '-'),
(40, 'Marcos', 'Florentin', 68, 'Nora', 8, 15786666, 45896531, 'marcos.fl@hotmail.com', 1123669868, 'nazarre 3545', '', '1953-05-05', '2021-11-01', '-'),
(41, 'Ramon', 'Carrizo', 32, '-', 10, 2024569855, 24569855, 'carrizom@gmail.com', 1127589955, 'Avenida Nazca 2100', '', '1989-05-01', '2021-11-05', '-'),
(44, 'Tomas Ricardo', 'Lujan', 16, 'Omar Perez', 11, 45236879, 59842366, 'tomas@gmail.com', 1145682387, 'Ramos Mejía', 'Parálisis Cerebral', '2008-12-15', '2022-10-04', 'Reflejos leves'),
(45, 'Malena', 'Caseres', 31, '-', 1, 452169, 36568468, 'malena@gmail.com', 297425986, 'Puerto Deseado', 'Ansiedad y depresión', '1991-02-19', '2022-10-04', 'Turno online semanal'),
(46, 'Jesus', 'Restrepo', 45, '-', 10, 0, 28451236, 'jesusrestrepo@gmail.com', 1145632787, 'Carabobo 73', 'Dislexia', '1949-06-19', '2022-10-04', 'Tratamiento'),
(47, 'Lorena', 'Carcamo', 65, '-', 9, 0, 5416105, '-', 114570614, 'Nazca 315 2 A', 'Acumuladora', '1935-11-19', '2022-10-01', 'Reconoce problema de acumulación por apego'),
(48, 'Edi', 'Cruz', 28, '-', 1, 0, 38125478, 'edi@gmail.com', 1155217485, 'Villa Luzuriaga', 'Obsesión compulsiva', '1996-12-18', '2022-10-05', 'Se presenta con su abuela a la consulta'),
(52, 'Tomas', 'Ruiz', 0, '', 1, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(53, 'Edito', '', 45, '', 1, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(54, 'Nora', 'Avila', 0, 'avila@gmail.com', 1, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(55, 'a', 'a', 1, 'a', 1, 11, 32112321, 'aa', 8888, 'aa', 'aaa', '2022-10-07', '2022-10-28', 'a'),
(56, 'aaaa', 'aaaa', 1, 'aaaa', 1, 1, 1, 'aaaa', 11, 'aaaa', 'aaaa', '2022-10-01', '2022-11-02', 'aaaa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesional`
--

CREATE TABLE `profesional` (
  `id_profesional` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `dni` int(11) NOT NULL,
  `telefono` int(15) NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `titulo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `institucion_educativa` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `es_prestador` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `id_obra_social` int(11) NOT NULL,
  `esta_matriculado` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `matricula` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `repetir_contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `profesional`
--

INSERT INTO `profesional` (`id_profesional`, `nombre`, `apellido`, `dni`, `telefono`, `direccion`, `email`, `titulo`, `institucion_educativa`, `es_prestador`, `id_obra_social`, `esta_matriculado`, `matricula`, `contraseña`, `repetir_contraseña`) VALUES
(1, 'Nora', 'Barria', 36661499, 1126332484, 'Miguel de Salcedo 1234', 'norabarria1@gmail.com', 'Técnico Superior de Análisis de Sistemas', 'UBA', 'No', 1, 'Si', '133326', '12345', '12345'),
(2, 'Ramon', 'Perez', 24561230, 2147483647, '25 de Mayo 361', 'ramon1@gmail.com', 'Psicólogo', 'UAI', 'No', 1, 'Si', '6325', 'ramon', 'ramon'),
(3, 'Flavio', 'Garrido', 20808080, 12345678, 'Lascano 4044', 'flavio.garrido@bue.edu.ar', 'Ingeniero de Software', 'UTN', '', 1, '', '', 'flavio16\r\n', 'flavio16\r\n'),
(4, 'Manuel', 'Buceta', 20808080, 12345678, 'Lascano 4044', 'vorgriff@gmail.com', 'Ingeniero de Software', 'UTN', '', 1, '', '', '123456', '123456'),
(5, 'asd', 'asd', 12312312, 1231231, 'asd', 'norabarria33@gmail.com', 'asd', 'xcvcxv', 'No', 7, 'no', '133326', '123', '123'),
(6, 'Federico', 'Barria', 36618055, 1126335562, 'Lobos 123', 'fede@gmail.com', 'Psicologo', 'UBA', 'Si', 12, 'no', '0', '555', '555'),
(7, 'Barbara', 'Nair', 36614044, 2147483647, 'Lascano 4044', 'barbara@gmail.com', 'Psicologo', 'UBA', 'No', 2, 'Si', '133329', '4848', '4848'),
(8, 'Belen', 'Aguirre', 36612258, 2147483647, 'Lobos 3568', 'belen@gmail.com', 'Fonoudiologo', 'UBA', 'Si', 6, 'Si', '133886', '6565', '6565'),
(9, 'ttt', 'tt', 366140, 1155555, 'Mio 1514', '55@gmail.com', 'Fonoudiologo', 'rr', 'Si', 6, 'no', '0', '33', '33'),
(10, 'rr', 'rr', 44, 54673, 'tt', 'gfd@gmail.com', 'Técnico Superior de Análisis de Sistemas', 'UBA', 'No', 1, 'no', '0', '2323', '2323'),
(11, 'rrr', 'rrr', 565, 33456, 'efd', 'uu1@gmail.com', 'tr', 'UBA', 'No', 1, '0', '0', '3434', '3434'),
(12, 'ew', 'ewe', 43, 34, 'rfwe', 'yy@gmail.com', '32', 'UBA', 'No', 1, '0', '0', '92', '92'),
(13, 'rr', 'rr', 54, 434, 'tt', 'pp@gmail.com', 'Psicologa', 'UBA', 'No', 1, 'no', '88', '88', '88'),
(14, 'rr', 'rr', 54, 434, 'tt', 'pp@gmail.com', 'Psicologa', 'UBA', 'No', 1, 'no', '88', '88', '88'),
(15, 'EE', 'EE', 44, 44, 'T', 'R@gmail.com', 'Psicologo', 'UBA', 'No', 1, 'no', '0', '21', '21'),
(16, 'TR', 'G', 66, 54, 'Y', 'yy@gmail.com', 'T', 'UBA', 'No', 1, '0', '1', '1', '1'),
(17, 'rr', 'rr', 3434, 5545, '34', '44', 'e', '334', 'No', 1, 'Si', '55', '11', '11'),
(18, 't', 't', 55, 55, 'tt', '5', 'e', 'e', 'No', 1, '5', '0', '6', '5'),
(19, 't', 't', 6, 6, '5', '8', 'Fonoudiologo', 'UBA', 'No', 1, '7', '7', '7', '7'),
(20, 'tt', 'ee', 454, 55, 'r', 'g@gmail.com', 't', 't', 'No', 1, 'Si', '55', '4', '4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sala_espera`
--

CREATE TABLE `sala_espera` (
  `id` int(11) NOT NULL,
  `en_espera` int(11) NOT NULL,
  `atendidos` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `sala_espera`
--

INSERT INTO `sala_espera` (`id`, `en_espera`, `atendidos`, `fecha`) VALUES
(1, 4, 0, '2022-10-31');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agenda`
--
ALTER TABLE `agenda`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `contactenos`
--
ALTER TABLE `contactenos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `obra_social`
--
ALTER TABLE `obra_social`
  ADD PRIMARY KEY (`id_obra_social`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_paciente_osid` (`id_obra_social`);

--
-- Indices de la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD PRIMARY KEY (`id_profesional`),
  ADD KEY `fk_profesional_osid` (`id_obra_social`);

--
-- Indices de la tabla `sala_espera`
--
ALTER TABLE `sala_espera`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agenda`
--
ALTER TABLE `agenda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `contactenos`
--
ALTER TABLE `contactenos`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `obra_social`
--
ALTER TABLE `obra_social`
  MODIFY `id_obra_social` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `profesional`
--
ALTER TABLE `profesional`
  MODIFY `id_profesional` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `sala_espera`
--
ALTER TABLE `sala_espera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `fk_paciente_osid` FOREIGN KEY (`id_obra_social`) REFERENCES `obra_social` (`id_obra_social`);

--
-- Filtros para la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD CONSTRAINT `fk_profesional_osid` FOREIGN KEY (`id_obra_social`) REFERENCES `obra_social` (`id_obra_social`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
