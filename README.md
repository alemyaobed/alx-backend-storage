# 0x00. MySQL Advanced

This repository contains advanced topics and exercises related to MySQL. It is part of the ALX Backend Storage curriculum.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)
6. [Resources](#resources)
7. [Learning Objectives](#learning-objectives)
8. [Requirements](#requirements)
9. [More Info](#more-info)

## Introduction
In this repository, you will find advanced concepts and exercises to enhance your understanding of MySQL. These topics cover more complex queries, performance optimization, indexing, stored procedures, triggers, views, functions and operators.

## Installation
To get started, make sure you have MySQL 5.7 installed on your machine. You can download the latest version from the official MySQL website. This project is tested on Ubuntu 18.04 LTS.

## Usage
Once you have MySQL installed, you can clone this repository and explore the different topics and exercises. Each topic is organized in its own directory, containing relevant files and instructions.

## Contributing
Contributions to this repository are welcome. If you have any improvements or additional exercises to share, feel free to submit a pull request.

## License
This repository is licensed under the [MIT License](LICENSE).

## Resources
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.mysqltutorial.org/mysql-index/mysql-indexing-best-practices/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/stored-programs-defining.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements
General:
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info
To run MySQL in a container, follow these steps:
1. Use "container-on-demand" to run MySQL
2. Ask for container Ubuntu 18.04 - Python 3.7
3. Connect via SSH or via the WebTerminal
4. Start MySQL in the container using the command: `$ service mysql start`
5. Import a SQL dump using the command: `$ echo "CREATE DATABASE database_name;" | mysql -uroot -p` followed by `$ curl "https://example.com/dump.sql" -s | mysql -uroot -p database_name`
6. Use the credentials `root/root` to access MySQL in the container.

Remember to replace `database_name` with the desired name for your database and `https://example.com/dump.sql` with the URL of the SQL dump you want to import.
