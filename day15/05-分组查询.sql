-- SELECT 字段列表 FROM 表名 GROUP BY 分组字段名
-- 以class_id进行分组
-- 注意: 使用了分组之后,select后面只能写分组的字段,或者聚合函数
SELECT class_id FROM student GROUP BY class_id;

-- 查询每个班级的学生人数
SELECT class_id,count(*) FROM student GROUP BY class_id;

-- 查询每个班级的平均年龄
SELECT class_id,AVG(stu_age) FROM student GROUP BY class_id;

-- 查询每个班级的最小年龄
SELECT MIN(stu_age) FROM student GROUP BY class_id;

-- 查询同一年龄的人数
SELECT stu_age, COUNT(*) FROM student GROUP BY stu_age;

-- SELECT 字段列表 FROM 表名 [ WHERE 条件 ] GROUP BY 分组字段名 [ HAVING 分组后过滤条件];
-- having 只能配合group by使用
-- 查询人数大于等于2的年龄
SELECT stu_age, COUNT(*) FROM student 
GROUP BY stu_age
HAVING COUNT(*) >= 2;

-- 查询班级人数大于3的班级
SELECT class_id, count(*) FROM student
GROUP BY class_id
HAVING COUNT(*) > 3;

-- 平均年龄大于30的班级
SELECT class_id FROM student
GROUP BY class_id
HAVING AVG(stu_age) > 30;

-- 对小于50岁的同学进行班级分组
SELECT class_id, COUNT(*) FROM student
WHERE stu_age < 50
GROUP BY class_id;

-- GROUP_CONCAT(expr) 对字段进行聚合，只能配合group by使用
-- 查询每个班级的学生姓名
SELECT class_id, GROUP_CONCAT(stu_name) FROM student
GROUP BY class_id;


