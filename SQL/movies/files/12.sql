SELECT movies.title FROM movies WHERE movies.id IN (SELECT stars.movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE stars.movie_id IN (SELECT stars.movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE people.name = "Helena Bonham Carter") AND people.name = "Johnny Depp")