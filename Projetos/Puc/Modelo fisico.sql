drop database if exists lanchonete;
create database lanchonete;
use lanchonete;

create table lanchonete.Pedido(
	codigo_Pedido int primary key,
    data_emissao date,
    status_em_preparacao varchar(45),
    status_em_entrega varchar(45),
    status_entregue varchar(45),
    foreign key(codigo) references lanchonete.Cliente(codigo),
    foreign key(codigo_item) references lanchonete.Lanches(codigo_item),
    foreign key(codigo_ent) references lanchonete.Entregadores(codigo)
);

create table lanchonete.Cliente(
	codigo int primary key,
    endereco varchar(45),
    nome varchar(45),
    telefone varchar(45),
    foreign key(codigo_Pedido) references lanchonete.Pedido(codigo_Pedido)
);


create table lanchonete.Lanches(
	codigo_item int primary key,
    nome varchar(45),
    valor decimal(3,2),
    foreign key(codigo_Pedido) references lanchonete.Pedido(codigo_Pedido)
);

create table lanchonete.Entregadores(
	codigo_ent int primary key,
	nome varchar(45),
	numero_telefone varchar(45),
	foreign key(codigo_Pedido) references lanchonete.Pedido(codigo_Pedido)
);
