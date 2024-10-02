Create Schema Final_Project;

use Final_Project;

create table Synthetic_data
(
Patient_ID int,
First_name varchar (255),
Last_name varchar(255),
Race varchar(255),
Weight double,
Height varchar(255),
Gender varchar(255),
primary key (Patient_ID)
);

create table User_Information
(
Patient_ID int,
First_name varchar (255),
Last_name varchar(255),
Race varchar(255),
Weight double,
Height varchar(255),
Gender varchar(255),
primary key (Patient_ID)
);

create table Disease
(
Patient_ID int,
Disease_ID int,
Disease_Name varchar(255),
Foreign key (Patient_ID) references Synthetic_Data(Patient_ID)
);



