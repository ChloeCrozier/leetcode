# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/
SELECT
	teacher_id, COUNT(DISTINCT subject_id) as cnts
FROM
	Teacher
GROUP BY
	teacher_id;
