-- lists cities in California which can be found in the database
SELECT id, name
FROM cities
WHERE state_id=
     (SELECT id
      FROM states
      WHERE name='California')
ORDER BY id;
