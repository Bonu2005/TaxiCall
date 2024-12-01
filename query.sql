create database  Order_a_taxi; 
use Order_a_taxi;
create table for_client(
name text,
phone_number text,
password text 
);
create table for_driver(
name text,
age int,
gender text,
model_of_car text,
phone_number text,
password text
);
create table orders(
id int auto_increment primary key,
client_name text,
from_where text,
where_to text,
date_of_order datetime,
status_of_order text,
driver_name text
);
