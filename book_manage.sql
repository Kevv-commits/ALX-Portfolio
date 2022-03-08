--setting up the database and the tables necessary for the system
create database db;

create table books(
    bid varchar(30) primary key not null,
    title varchar(30) not null,
    author varchar(30) not null,
    status varchar(30) not null
);

create table books_issued(
    bid varchar(20) primary key not null,
    issuedto varchar(50) not null
);
