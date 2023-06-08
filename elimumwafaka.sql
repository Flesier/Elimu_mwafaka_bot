-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 08, 2023 at 11:18 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elimumwafaka`
--

-- --------------------------------------------------------

--
-- Table structure for table `maths_progress`
--

CREATE TABLE `maths_progress` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `column1` int(11) DEFAULT NULL,
  `column2` int(11) DEFAULT NULL,
  `column3` int(11) DEFAULT NULL,
  `column4` int(11) DEFAULT NULL,
  `column5` int(11) DEFAULT NULL,
  `column6` int(11) DEFAULT NULL,
  `column7` int(11) DEFAULT NULL,
  `column8` int(11) DEFAULT NULL,
  `column9` int(11) DEFAULT NULL,
  `column10` int(11) DEFAULT NULL,
  `column11` int(11) DEFAULT NULL,
  `column12` int(11) DEFAULT NULL,
  `column13` int(11) DEFAULT NULL,
  `column14` int(11) DEFAULT NULL,
  `column15` int(11) DEFAULT NULL,
  `column16` int(11) DEFAULT NULL,
  `column17` int(11) DEFAULT NULL,
  `column18` int(11) DEFAULT NULL,
  `column19` int(11) DEFAULT NULL,
  `column20` int(11) DEFAULT NULL,
  `column21` int(11) DEFAULT NULL,
  `column22` int(11) DEFAULT NULL,
  `column23` int(11) DEFAULT NULL,
  `column24` int(11) DEFAULT NULL,
  `column25` int(11) DEFAULT NULL,
  `column26` int(11) DEFAULT NULL,
  `column27` int(11) DEFAULT NULL,
  `column28` int(11) DEFAULT NULL,
  `column29` int(11) DEFAULT NULL,
  `column30` int(11) DEFAULT NULL,
  `column31` int(11) DEFAULT NULL,
  `column32` int(11) DEFAULT NULL,
  `column33` int(11) DEFAULT NULL,
  `column34` int(11) DEFAULT NULL,
  `column35` int(11) DEFAULT NULL,
  `column36` int(11) DEFAULT NULL,
  `column37` int(11) DEFAULT NULL,
  `column38` int(11) DEFAULT NULL,
  `column39` int(11) DEFAULT NULL,
  `column40` int(11) DEFAULT NULL,
  `column41` int(11) DEFAULT NULL,
  `column42` int(11) DEFAULT NULL,
  `column43` int(11) DEFAULT NULL,
  `column44` int(11) DEFAULT NULL,
  `column45` int(11) DEFAULT NULL,
  `column46` int(11) DEFAULT NULL,
  `column47` int(11) DEFAULT NULL,
  `column48` int(11) DEFAULT NULL,
  `column49` int(11) DEFAULT NULL,
  `column50` int(11) DEFAULT NULL,
  `column51` int(11) DEFAULT NULL,
  `column52` int(11) DEFAULT NULL,
  `column53` int(11) DEFAULT NULL,
  `column54` int(11) DEFAULT NULL,
  `column55` int(11) DEFAULT NULL,
  `column56` int(11) DEFAULT NULL,
  `column57` int(11) DEFAULT NULL,
  `column58` int(11) DEFAULT NULL,
  `column59` int(11) DEFAULT NULL,
  `column60` int(11) DEFAULT NULL,
  `column61` int(11) DEFAULT NULL,
  `column62` int(11) DEFAULT NULL,
  `column63` int(11) DEFAULT NULL,
  `column64` int(11) DEFAULT NULL,
  `column65` int(11) DEFAULT NULL,
  `column66` int(11) DEFAULT NULL,
  `column67` int(11) DEFAULT NULL,
  `column68` int(11) DEFAULT NULL,
  `column69` int(11) DEFAULT NULL,
  `column70` int(11) DEFAULT NULL,
  `column71` int(11) DEFAULT NULL,
  `column72` int(11) DEFAULT NULL,
  `column73` int(11) DEFAULT NULL,
  `column74` int(11) DEFAULT NULL,
  `column75` int(11) DEFAULT NULL,
  `column76` int(11) DEFAULT NULL,
  `column77` int(11) DEFAULT NULL,
  `column78` int(11) DEFAULT NULL,
  `column79` int(11) DEFAULT NULL,
  `column80` int(11) DEFAULT NULL,
  `column81` int(11) DEFAULT NULL,
  `column82` int(11) DEFAULT NULL,
  `column83` int(11) DEFAULT NULL,
  `column84` int(11) DEFAULT NULL,
  `column85` int(11) DEFAULT NULL,
  `column86` int(11) DEFAULT NULL,
  `column87` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `prompts`
--

CREATE TABLE `prompts` (
  `id` int(254) NOT NULL,
  `topic` varchar(254) NOT NULL,
  `question_id` varchar(254) NOT NULL,
  `question` varchar(254) NOT NULL,
  `answer_id` varchar(254) NOT NULL,
  `answer` varchar(254) NOT NULL,
  `user_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `adm` varchar(255) DEFAULT NULL,
  `parent` varchar(255) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `parent_phone` varchar(255) DEFAULT NULL,
  `paid` enum('Yes','No') DEFAULT NULL,
  `last_point` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `current_school` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `progress` int(11) DEFAULT NULL,
  `classe` enum('1','2','3','4') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `username`, `first_name`, `last_name`, `adm`, `parent`, `parent_id`, `parent_phone`, `paid`, `last_point`, `password`, `current_school`, `location`, `progress`, `classe`) VALUES
(1, 'john', 'John', 'Simiyu', 'john.sim@example.com', 'Parent 1', 12345, '123-456-7890', 'Yes', 80, 'password1234', 'Meru Boys High School', 'Nakuru', 3, '3'),
(2, 'Wambui', 'Jane', 'wambu', 'jane.wambu@example.com', 'Parent 2', 67890, '987-654-3210', 'No', 65, 'password2234', 'Pangani Girls high School', 'Nakuru', 2, '2');

-- --------------------------------------------------------

--
-- Table structure for table `topics`
--

CREATE TABLE `topics` (
  `id` int(11) NOT NULL,
  `form` int(11) DEFAULT NULL,
  `topic_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `topics`
--

INSERT INTO `topics` (`id`, `form`, `topic_name`) VALUES
(1, 1, 'Whole Numbers'),
(2, 1, 'Integers'),
(3, 1, 'Fractions'),
(4, 1, 'Decimals'),
(5, 1, 'Factors and Multiples'),
(6, 1, 'Ratio, Proportion, and Rate'),
(7, 1, 'Percentages'),
(8, 1, 'Measurement'),
(9, 1, 'Algebraic Expressions'),
(10, 1, 'Angles'),
(11, 1, 'Quadrilaterals'),
(12, 1, 'Circles'),
(13, 1, 'Three-Dimensional Figures'),
(14, 1, 'Statistics and Probability'),
(15, 1, 'Simultaneous Linear Equations'),
(16, 1, 'Indices and Logarithms'),
(17, 1, 'Expansion and Factorization of Algebraic Expressions'),
(18, 1, 'Simple and Compound Interest'),
(19, 1, 'Consumer Arithmetic'),
(20, 1, 'Data Handling'),
(21, 2, 'Quadrilaterals'),
(22, 2, 'Circles'),
(23, 2, 'Three-Dimensional Figures'),
(24, 2, 'Statistics and Probability'),
(25, 2, 'Simultaneous Linear Equations'),
(26, 2, 'Indices and Logarithms'),
(27, 2, 'Expansion and Factorization of Algebraic Expressions'),
(28, 2, 'Simple and Compound Interest'),
(29, 2, 'Consumer Arithmetic'),
(30, 2, 'Data Handling'),
(31, 2, 'Linear Equations and Inequalities'),
(32, 2, 'Functions'),
(33, 2, 'Mensuration'),
(34, 2, 'Trigonometry'),
(35, 2, 'Matrices'),
(36, 2, 'Sets and Venn Diagrams'),
(37, 2, 'Quadratic Equations'),
(38, 2, 'Probability'),
(39, 2, 'Indices, Logarithms, and Exponential Functions'),
(40, 2, 'Variation'),
(41, 3, 'Quadratic Equations'),
(42, 3, 'Probability'),
(43, 3, 'Indices, Logarithms, and Exponential Functions'),
(44, 3, 'Variation'),
(45, 3, 'Coordinate Geometry'),
(46, 3, 'Plane Geometry'),
(47, 3, 'Trigonometry'),
(48, 3, 'Statistics'),
(49, 3, 'Matrices and Transformations'),
(50, 3, 'Arithmetic and Geometric Progressions'),
(51, 3, 'Calculus'),
(52, 3, 'Financial Mathematics'),
(53, 3, 'Set Theory'),
(54, 3, 'Probability Distributions'),
(55, 3, 'Geometry of Circles'),
(56, 3, 'Data Analysis and Presentation'),
(57, 3, 'Indices and Surds'),
(58, 3, 'Functions and Graphs'),
(59, 4, 'Trigonometry'),
(60, 4, 'Calculus'),
(61, 4, 'Financial Mathematics'),
(62, 4, 'Set Theory'),
(63, 4, 'Probability Distributions'),
(64, 4, 'Geometry of Circles'),
(65, 4, 'Data Analysis and Presentation'),
(66, 4, 'Indices and Surds'),
(67, 4, 'Functions and Graphs'),
(68, 4, 'Vectors'),
(69, 4, 'Probability and Statistics'),
(70, 4, 'Geometry of Triangles'),
(71, 4, 'Linear Programming'),
(72, 4, 'Matrices and Transformations'),
(73, 4, 'Sequences and Series'),
(74, 4, 'Differentiation and Integration'),
(75, 4, 'Index Numbers'),
(76, 4, 'Geometry of Solids'),
(77, 4, 'Further Calculus'),
(78, 4, 'Coordinate Geometry'),
(79, 4, 'Linear Algebra'),
(80, 4, 'Trigonometric Equations'),
(81, 4, 'Financial Applications'),
(82, 4, 'Statistics and Probability'),
(83, 4, 'Differential Equations'),
(84, 4, 'Indices and Logarithms'),
(85, 4, 'Complex Numbers'),
(86, 4, 'Statistics'),
(87, 4, 'Business Mathematics');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `maths_progress`
--
ALTER TABLE `maths_progress`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `topics`
--
ALTER TABLE `topics`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `maths_progress`
--
ALTER TABLE `maths_progress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `topics`
--
ALTER TABLE `topics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
