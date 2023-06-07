-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2023 at 09:53 AM
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
