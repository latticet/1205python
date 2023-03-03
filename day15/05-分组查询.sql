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

-- 


