-- alter table 从表 add [constraint 约束名字] foreign key (外键字段) references 主表(关联字段) 
ALTER TABLE student ADD FOREIGN KEY(class_id)
REFERENCES class(class_id);

-- 查看外键
show CREATE TABLE student;

-- 删除外键
-- ALTER TABLE student DROP FOREIGN KEY 约束名称;
ALTER TABLE student DROP FOREIGN KEY student_ibfk_1;