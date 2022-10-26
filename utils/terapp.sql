-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2022 a las 01:51:12
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

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
-- Estructura de tabla para la tabla `especialidad`
--

/* CREATE TABLE `especialidad` (
  `id_especialidad` int(11) NOT NULL,
  `nombre` varchar(40) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci */;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `obra_social`
--

CREATE TABLE `obra_social` (
  `id_obra_social` int(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `activo` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `obra_social`
--

INSERT INTO `obra_social` (`id_obra_social`, `nombre`, `activo`) VALUES
(1, 'Galeno', 1),
(2, 'Medicus', 1),
(3, 'Osseg', 1),
(4, 'Opdea', 1),
(5, 'Sadiac', 1),
(6, 'Hominis', 1),
(7, 'Osdipp', 1),
(8, 'Ospic', 1),
(9, 'Elevar', 1),
(10, 'Medicus', 1);

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
  `obra_social` int(10) NOT NULL,
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

INSERT INTO `paciente` (`id`, `nombre`, `apellido`, `edad`, `tutor`, `obra_social`, `n_afiliado`, `dni`, `email`, `telefono`, `domicilio`, `diagnostico`, `fecha_de_nacimiento`, `fecha_de_ingreso`, `observaciones`) VALUES
(34, 'Nora', 'Barria', 20, '-', 0, 1245648, 36645898, 'nora.barria@gmail.com', 48702654, 'Nueva York 123', '-', '1990-05-08', '2021-02-12', '-'),
(35, 'Marcos', 'Gutierrez', 24, '-', 0, 2147483647, 12345678, 'marcos.gutierrez@hotmail.com', 1557263899, 'Bahia Blanca 2620', '-', '1997-07-03', '2021-11-01', '-'),
(36, 'Gonzalo', 'Galarza', 28, 'Nora Barria', 0, 21888456, 35000856, 'gonzalo.galarza@yahoo.com', 48705698, 'Lascano 123', '-', '1993-11-10', '2021-11-10', '-'),
(37, 'Maria', 'Eizayaga', 26, '-', 0, 541567893, 38589753, 'maria.eizayaga@outlook.com', 1587963255, 'Concordia 2587', '-', '1995-11-11', '2021-11-16', '-'),
(38, 'Francisco', 'Ceccoli', 47, '-', 0, 123501264, 20123582, 'francisco.ceccoli@msn.com', 45896235, 'Sanabria 789', '-', '1975-01-01', '2021-11-01', '-'),
(39, 'Lidia', 'Medina', 51, '-', 0, 1, 11263324, 'medinalidia3@gmail.com', 42058978, 'Nazarre 3487', '-', '1960-06-02', '2021-11-01', '-'),
(40, 'Marcos', 'Florentin', 68, 'Nora', 0, 15786666, 45896531, 'marcos.fl@hotmail.com', 1123669868, 'nazarre 3545', '', '1953-05-05', '2021-11-01', '-'),
(41, 'Ramon', 'Carrizo', 32, '-', 0, 2024569855, 24569855, 'carrizom@gmail.com', 1127589955, 'Avenida Nazca 2100', '', '1989-05-01', '2021-11-05', '-'),
(44, 'Tomas Ricardo', 'Lujan', 16, 'Omar Perez', 0, 45236879, 59842366, 'tomas@gmail.com', 1145682387, 'Ramos Mejía', 'Parálisis Cerebral', '2008-12-15', '2022-10-04', 'Reflejos leves'),
(45, 'Malena', 'Caseres', 31, '-', 0, 452169, 36568468, 'malena@gmail.com', 297425986, 'Puerto Deseado', 'Ansiedad y depresión', '1991-02-19', '2022-10-04', 'Turno online semanal'),
(46, 'Jesus', 'Restrepo', 45, '-', 0, 0, 28451236, 'jesusrestrepo@gmail.com', 1145632787, 'Carabobo 73', 'Dislexia', '1949-06-19', '2022-10-04', 'Tratamiento'),
(47, 'Lorena', 'Carcamo', 65, '-', 0, 0, 5416105, '-', 114570614, 'Nazca 315 2 A', 'Acumuladora', '1935-11-19', '2022-10-01', 'Reconoce problema de acumulación por apego'),
(48, 'Edi', 'Cruz', 28, '-', 0, 0, 38125478, 'edi@gmail.com', 1155217485, 'Villa Luzuriaga', 'Obsesión compulsiva', '1996-12-18', '2022-10-05', 'Se presenta con su abuela a la consulta'),
(52, 'Tomas', 'Ruiz', 0, '', 0, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(53, 'Edito', '', 45, '', 0, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(54, 'Nora', 'Avila', 0, 'avila@gmail.com', 0, 0, 0, '', 0, '', '', '0000-00-00', '0000-00-00', ''),
(55, 'a', 'a', 1, 'a', 0, 11, 32112321, 'aa', 8888, 'aa', 'aaa', '2022-10-07', '2022-10-28', 'a'),
(56, 'aaaa', 'aaaa', 1, 'aaaa', 0, 1, 1, 'aaaa', 11, 'aaaa', 'aaaa', '2022-10-01', '2022-11-02', 'aaaa');

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
  `obra_social` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `esta_matriculado` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `matricula` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `repetir_contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `profesional`
--

INSERT INTO `profesional` (`id_profesional`, `nombre`, `apellido`, `dni`, `telefono`, `direccion`, `email`, `titulo`, `es_prestador`, `obra_social`, `institucion_educativa`, `esta_matriculado`, `matricula`, `contraseña`, `repetir_contraseña`) VALUES
(1, 'Nora', 'Barria', 36661499, 1126332484, 'Miguel de Salcedo 1234', 'norabarria1@gmail.com', 'Técnico Superior de Análisis de Sistemas', 'Si', 'smg', 'UBA', 'Si', '133326', '12345', '12345'),
(2, 'Ramon', 'Perez', 24561230, 2147483647, '25 de Mayo 361', 'ramon1@gmail.com', 'Psicólogo', 'No', '-', 'UAI', 'Si', '6325', 'ramon', 'ramon');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `especialidad`
--
/*ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id_especialidad`)*/;

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `profesional`
--
ALTER TABLE `profesional`
  ADD PRIMARY KEY (`id_profesional`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `especialidad`
--
/*ALTER TABLE `especialidad`
  MODIFY `id_especialidad` int(11) NOT NULL AUTO_INCREMENT*/;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `profesional`
--
ALTER TABLE `profesional`
  MODIFY `id_profesional` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

