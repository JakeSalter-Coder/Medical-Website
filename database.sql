create database medicaldata;
use medicaldata;
create table patients(ID int,
					  first_name char(15),
                      last_name char(15),
					  race char(15), 
					  age int, 
                      gender char(10), 
                      weight int, 
                      height double, 
                      disease char(35));
                      
select * from patients