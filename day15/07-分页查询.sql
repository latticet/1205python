-- SELECT 字段列表 FROM 表名 LIMIT 起始索引, 查询记录数;   
-- 起始索引：默认是从0开始
-- limit 1, 2

SELECT * FROM student limit 0, 3;
-- SELECT * FROM student where stu_id = 1 or stu_id = 3;
-- SELECT * FROM student where stu_id in (1, 3);


# 当前第几页   每页显示多少条(2)
# 1 			  limit 0, 2
# 2  				limit 2, 2
# 3					limit 4, 2
# 4  				limit 6, 2
						
# 				偏移量：(当前页 - 1) * 每页显示条数


