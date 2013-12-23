登录 mysql -h 主机名 -u 用户名 -p 密码  
show databases;  
use 数据库名  
show tables;  
create table 表名(  
    id int primary key,
    name char(30) not null
);
insert into 表名 values(1,2,3,...);  
select * from 表名;  
