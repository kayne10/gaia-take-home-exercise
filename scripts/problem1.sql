-- Question 1
SELECT vv.video_id, COUNT(vv.user_id) AS num_users_watched
FROM video_views as vv
GROUP BY vv.video_id
HAVING DATEDIFF(SECOND, vv.view_start, vv.view_end) >= 10
ORDER BY num_users_watched DESC
LIMIT 5;


-- Question 2
SELECT vv.video_id, v.title, SUM(DATEDIFF(SECOND, vv.view_start, vv.view_end)) AS total_seconds_watched
FROM video_views AS vv,
INNER JOIN videos AS v
ON v.video_id = vv.video_id
GROUP BY v.video_id;
