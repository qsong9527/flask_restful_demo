
USE db_users;

DROP TABLE IF EXISTS tb_user;

CREATE TABLE tb_user (
	id int primary key auto_increment comment 'user id',
    username varchar(20) not null comment 'user name',
    email varchar(20) not null unique comment 'user email address',
    tel varchar(11) not null unique comment 'user tel phone no.',
    password varchar(20) comment 'user password store by secrect',
    gender varchar(1) comment '0 null, 1 male, 2 female',
    active boolean comment 'true: active, false inactive',
    create_time datetime default current_timestamp comment 'user create time'
);
-- desc tb_user；