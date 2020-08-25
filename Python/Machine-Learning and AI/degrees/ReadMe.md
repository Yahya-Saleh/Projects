# Degrees

A program that determines how many “degrees of separation” apart two actors are. [Watch an illustration!](https://www.youtube.com/watch?v=CRNSMGsmEqo&t=8s)

## Usage

```bash
$ python degrees.py large
Loading data...
Data loaded.

Name: Emma Watson
Name: Jennifer Lawrence

3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Table of contents

- [Degrees](#degrees)
  - [Usage](#usage)
  - [Table of contents](#table-of-contents)
  - [Six Degrees of Kevin Bacon](#six-degrees-of-kevin-bacon)
  - [Search algorithm](#search-algorithm)
  - [DataBase](#database)
    - [movies.csv](#moviescsv)
    - [people.csv](#peoplecsv)
    - [stars.csv](#starscsv)
  - [Util.py](#utilpy)
    - [node](#node)
    - [QueueFrontier](#queuefrontier)
      - [Attributes](#attributes)
      - [Methods](#methods)
  - [Degree.py](#degreepy)
    - [shortest path](#shortest-path)
    - [expand node](#expand-node)
    - [get path](#get-path)
  - [Acknowledgements](#acknowledgements)

---

## Six Degrees of Kevin Bacon

According to the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.

This program uses a **breadth-first search algorithm** to find the shortest path between any two given actors.

## Search algorithm

We can frame this as a search problem: our states are people. Our actions are movies, which take us from one actor to another. Our initial state and goal state are defined by the two people we’re trying to connect. By using **breadth-first search**, we can find the shortest path from one actor to another.

---

## DataBase

This program uses two sets of CSV data files: stored in the small and large folders. the two folders hold the same set of CSV files except the former has less data for the sake of experiment and testing. The information that the CSV files hold are based on [IMDb](https://www.imdb.com/)'s database.

### movies.csv

| id     | title       | year |
| ------ | ----------- | ---- |
| 112384 | "Apollo 13" | 1995 |

This file has a list of movies' `titles` and `year of release` all uniquely identified with an `id`.

### people.csv

| id  | name         | birth |
| --- | ------------ | ----- |
| 129 | "Tom Cruise" | 1962  |

Holds an `id` corresponding to the `name` and `year of birth` of actors.

### stars.csv

| person_id | movie_id |
| --------- | -------- |
| 129       | 112384   |

This file acts as a bridge table connecting each actor to the movies they starred in using their ids: `person_id` and `movie_id` respectively.

---

## [Util.py](util.py)

This python file defines the classes used in the main program.

### node

This class simply holds three elements: a state, the state that generated it, and the action take from the parent state. For this project our states are `person_id`s, and our actions are `movie_id`s.

### QueueFrontier

Since we want to find the optimal path between two given nodes, we'll implement a Breadth-first search which uses a `Queue` data structure. the QueueFrontier class inherits the same methods and attributes of the Stack Frontier, except the way it removes nodes is different.

#### Attributes

This frontier has two attributes allowing it to store nodes to be explored and ones that already are: frontier and explored respectively.

#### Methods

The class can add nodes, check if a node is in the frontier or if it is explored, remove nodes, and tell if it is empty.

## [Degree.py](degrees.py)

If you go through the file you will find logic implemented to load a given database and take two names from the user after resolving any conflict, but let us focus our attention on where Breadth-first search is implemented.

### shortest path

This function creates a QueueFrontier and adds the source node to the frontier then initiates a loop that will terminate when the frontier is empty. Inside the loop, the program removes the first node in and expand it calling the `expand_node` function. If a solution is found the path is returned otherwise the loop resumes.

### expand node

This function takes in a frontier, source node, and the targeted id. Using the input, function generate a tuple of all actors connected to the source node,(movie_id, person_id), and checks if the target is among them. If the target is indeed found it returns the path of the target node using the `get_path` function, otherwise this function adds the tuples as nodes to the frontier.

### get path

Takes in a node and returns the taken from the first to reach that node.

---

## Acknowledgements

[util.py](util.py), and some functions of [degrees.py](degrees.py)- load_data, main, person_id_for_name, and neighbors_for_person - were provided by CS50AI. Information courtesy of [IMDb](https://www.imdb.com/). Used with permission.
