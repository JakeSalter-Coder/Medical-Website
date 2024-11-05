Create Schema if not exists Final_Project;

use Final_Project;

create table if not exists Disease
(
Disease_ID int,
Disease_Name varchar(255),
primary key (Disease_ID)
);

create table if not exists Synthetic_data
(
Patient_ID varchar(255),
First_name varchar (255),
Last_name varchar(255),
Race varchar(255),
Weight double,
Height varchar(255),
Gender varchar(255),
Obesity bool,
Disease_ID int,
primary key (Patient_ID),
Foreign key (Disease_ID) references Disease(Disease_ID)
);

create table if not exists User_Information
(
Patient_ID varchar(255),
First_name varchar (255),
Last_name varchar(255),
Race varchar(255),
Weight double,
Height varchar(255),
Gender varchar(255),
Obesity bool,
Disease_ID int,
primary key (Patient_ID),
Foreign key (Disease_ID) references Disease(Disease_ID)
);

