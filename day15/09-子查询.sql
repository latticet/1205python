-- select xxxx  select xxxx
/*
-- 标量： 单行单列
SELECT stu_name FROM student where stu_name = '张飞'
-- 列: 返回的数据只有一列
SELECT stu_name FROM student;
-- 行：返回的数只有一行
SELECT * FROM student WHERE stu_name = '张飞';
-- 表: 多行多列
SELECT * FROM student;
*/

-- 标量子查询
-- 查询class_id=1这个班级最大的人,年龄最大的人
-- 1. 通过班级id获取最大的年龄
SELECT MAX(stu_age) FROM student WHERE class_id = 1;
-- 2. 通过年龄查询对应的姓名
SELECT stu_name FROM student WHERE stu_age = 43;
-- 子查询
SELECT stu_name FROM student WHERE stu_age = 
(SELECT MAX(stu_age) FROM student WHERE class_id = 1)

-- 查询1班所有的学生姓名
-- 1. 通过班级名称查询班级id
SELECT class_id FROM class WHERE class_name = '1班';
-- 2. 通过班级id查询对应学生
SELECT stu_name FROM student WHERE class_id = 1;
-- 子查询
SELECT stu_name FROM student WHERE class_id = 
(SELECT class_id FROM class WHERE class_name = '2班');

-- 列子查询
-- 查询1班和2班所有学生信息
-- 1. 通过班级名称查询班级id
SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班';
-- 2. 通过班级id查询学生信息
SELECT * FROM student WHERE class_id = 1 or class_id = 2;
-- 子查询
SELECT * FROM student WHERE class_id in 
(SELECT class_id FROM class WHERE class_name = '1班' OR class_name = '2班');


-- 行子查询
-- 查询class_id=1这个班级最大的人,年龄最大的人
-- 1. 查询最大年龄和班级，通过class_id
SELECT class_id, max(stu_age) FROM student WHERE class_id = 1;
-- 2. 根据班级id和最大年龄查询对应的人
SELECT stu_name FROM student WHERE class_id = 1 AND stu_age = 43;
-- 子查询
SELECT stu_name FROM student WHERE (class_id, stu_age) = 
(SELECT class_id, max(stu_age) FROM student WHERE class_id = 1);


