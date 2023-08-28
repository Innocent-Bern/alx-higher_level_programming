-- script that list cities of Carlifonia in database hbtn_0d_usa

SELECT id, name
FROM cities WHERE state_id = (
	SELECT id 
	FROM states WHERE name = 'Calfornia'
)
ORDER BY id ASC;
