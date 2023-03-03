-- SELECT 字段列表 FROM 表名 WHERE 条件列表;
-- 比较运算符
-- 查询id大于3的学生信息
SELECT * FROM student WHERE stu_id > 3;

-- 逻辑运算符
SELECT * FROM student WHERE stu_id > 3 OR class_id = 1;


-- 模糊查询
-- %: 任意多个字符
SELECT * FROM student WHERE stu_name like '张%';
-- _：任意一个字符
SELECT * FROM student WHERE stu_name like '张_';

-- 范围查询
-- 字段 between .. and ..表示在一个连续的范围内查询
SELECT * FROM student WHERE stu_id BETWEEN 3 AND 6;

-- 字段 not between .. and ..表示连续范围取反
SELECT * FROM student WHERE stu_id NOT BETWEEN 3 AND 6;

-- 字段 in (value1, ...) 表示在一个非连续的范围内查询
SELECT * FROM student WHERE stu_no 
IN ('itsrc-003', 'itsrc-012', 'itsrc-014');

-- not in表示非连续的范围取反
SELECT * FROM student WHERE stu_no 
NOT IN ('itsrc-003', 'itsrc-012', 'itsrc-014');

-- 是否为空
-- is null
SELECT * FROM student WHERE stu_name IS NULL;
-- is not null
SELECT * FROM student WHERE stu_name IS NOT NULL;

