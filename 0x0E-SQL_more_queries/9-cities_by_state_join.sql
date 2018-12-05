-- List cities and their states
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities ON states.id=cities.state_id;
