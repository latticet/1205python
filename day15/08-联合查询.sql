-- UNION ALL 不去重
SELECT * FROM student WHERE stu_age >= 23
UNION ALL
SELECT * FROM student WHERE stu_age <= 23;

-- UNION 去重
SELECT * FROM student WHERE stu_age >= 23
UNION
SELECT * FROM student WHERE stu_age <= 23;


SELECT stu_age FROM student WHERE stu_age > 30
UNION
SELECT stu_age FROM student WHERE stu_age < 30;