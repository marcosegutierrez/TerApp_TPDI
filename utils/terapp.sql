-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-06-2022 a las 23:34:35
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.11

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
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `edad` int(11) NOT NULL,
  `tutor` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `obra_social` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
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
(34, 'Nora', 'Barria', 20, '-', 'Galeno', 1245648, 36645898, 'nora.barria@gmail.com', 48702654, 'Nueva York 123', '-', '1990-05-08', '2021-02-12', '-'),
(35, 'Marcos', 'Gutierrez', 24, '-', 'Osecac', 2147483647, 12345678, 'marcos.gutierrez@hotmail.com', 1557263899, 'Bahia Blanca 2620', '-', '1997-07-03', '2021-11-01', '-'),
(36, 'Gonzalo', 'Galarza', 28, 'Nora Barria', 'Galeno', 21888456, 35000856, 'gonzalo.galarza@yahoo.com', 48705698, 'Lascano 123', '-', '1993-11-10', '2021-11-10', '-'),
(37, 'Maria', 'Eizayaga', 26, '-', 'Swiss Medical', 541567893, 38589753, 'maria.eizayaga@outlook.com', 1587963255, 'Concordia 2587', '-', '1995-11-11', '2021-11-16', '-'),
(38, 'Francisco', 'Ceccoli', 47, '-', 'Medicus', 123501264, 20123582, 'francisco.ceccoli@msn.com', 45896235, 'Sanabria 789', '-', '1975-01-01', '2021-11-01', '-'),
(39, 'Lidia', 'Medina', 51, '-', '-', 1, 11263324, 'medinalidia3@gmail.com', 42058978, 'Nazarre 3487', '-', '1960-06-02', '2021-11-01', '-'),
(40, 'Marcos', 'Florentin', 68, 'Nora', 'Osde', 15786666, 45896531, 'marcos.fl@hotmail.com', 1123669868, 'nazarre 3545', '', '1953-05-05', '2021-11-01', '-'),
(41, 'Ramon', 'Carrizo', 32, '-', 'Osecac', 2024569855, 24569855, 'carrizom@gmail.com', 1127589955, 'Avenida Nazca 2100', '', '1989-05-01', '2021-11-05', '-'),
(42, 'Fabrizio', 'Avila', 24, '-', '-', 2, 24569855, 'avilaf@yahoo.com', 1589638626, 'cuenca 1230', '', '1997-01-25', '2021-11-10', '-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesional`
--

CREATE TABLE `profesional` (
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `dni` int(11) NOT NULL,
  `telefono` int(15) NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `titulo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `es_prestador` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `obra_social` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `institucion_educativa` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `esta_matriculado` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `matricula` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `repetir_contraseña` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `profesional`
--

INSERT INTO `profesional` (`nombre`, `apellido`, `dni`, `telefono`, `direccion`, `email`, `titulo`, `es_prestador`, `obra_social`, `institucion_educativa`, `esta_matriculado`, `matricula`, `contraseña`, `repetir_contraseña`) VALUES
('Nora', 'Barria', 36772320, 1567891022, 'San Miguel 2189', 'norabarria@gmail.com', 'Licenciada en Educación', 'SI', 'SMG', 'UBA', 'SI', '132698', '12345', '12345');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
