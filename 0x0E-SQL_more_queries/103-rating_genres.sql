-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.name FROM tv_shows, SUM('rate') AS 'rating'
JOIN tv_show_genre ON tv_show_rating.id=tv_show_genre.show_id
GROUP BY name
ORDER BY rating DESC;
