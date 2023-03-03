-- SELECT 聚合函数(字段列表) FROM 表名;
-- COUNT 聚合记录个数
SELECT COUNT(stu_name) FROM student;

-- SUM 聚合字段的和
SELECT SUM(stu_age) FROM student;

-- AVG 聚合字段的平均值
SELECT AVG(stu_age) FROM student;

-- MIN 聚合字典的最小值
SELECT MIN(stu_age) FROM student;

-- MAX 聚合字典的最大值
SELECT MAX(stu_age) FROM student;
