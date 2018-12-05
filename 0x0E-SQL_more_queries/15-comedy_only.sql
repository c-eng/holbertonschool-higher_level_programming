-- Selects comedy titles
SELECT tv_shows.title
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
WHERE genre_id=(
      SELECT id
      FROM tv_genres
      WHERE name='Comedy')
ORDER BY title;
