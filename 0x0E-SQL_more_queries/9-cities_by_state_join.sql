-- lists all cities contained in database
-- each record displays: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
