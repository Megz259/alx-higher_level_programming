-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title FROM tv_shows, SUM('rate') AS 'rating'
JOIN tv_show_rating ON tv_show.id=tv_show_rating.show_id
GROUP BY title
ORDER BY rating DESC;
