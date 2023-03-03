create database advanced;

create table student(
stu_id int unsigned not null primary key auto_increment comment '学生id',
stu_no char(10) not null unique key comment '学生学号',
stu_name varchar(20) comment '学生姓名',
class_id int unsigned comment '班级id'
)engine=innodb default charset=utf8 comment='学生表';

create table class(
class_id int unsigned not null primary key auto_increment comment '班级id',
class_name varchar(20) comment '班级名称',
class_room char(3) comment '班级教室'
)engine=innodb default charset=utf8 comment='班级表';