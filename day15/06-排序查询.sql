-- mysql存在默认排序，以id升序排列
SELECT * FROM student;
SELECT * FROM student WHERE stu_id in (6, 3, 1);

-- SELECT 字段列表 FROM 表名 ORDER BY 字段1 [排序方式] , 字段2 [排序方式], 字段N [排序方式];
-- 查询学生信息，年龄从小到大
SELECT * FROM student ORDER BY stu_age;
SELECT * FROM student ORDER BY stu_age ASC;

-- 查询学生信息，年龄从大到小
SELECT * FROM student ORDER BY stu_age DESC, stu_id DESC;



