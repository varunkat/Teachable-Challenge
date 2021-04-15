# NEIGHBORING NODES CHALLENGE

The below challenge is focused on constructing a nxn grid of defined size n consisting of (x,y) coordinates and index in the order of grid creation. Users can specify different parameters to know the coordinates, index position and print out neighborhood patterns (SQUARE, CROSS and DIAMOND) based on their requirements. A Database schema was designed by constructing different tables and assumptions and was discussed in detail in the below sections


## Development

This challenge was divided into three tasks and the detailed description for each task is provided below

### Task 1 - Build The Grid
* First task is about building a class that will accept two different parameters (size, debug) and adding methods to construct the grid and another method to return coordinates of the index
* The name of the class is mentioned below
```
class NeighboringNodes():

    def __init__(self, size, debug:bool):
```
* After the class is initiated, below method will create size x size grid with (x,y) coordinates and index values in the order of grid creation
```
 def create_grid(self):
```
* This algorithm was designed to assign coordinates from 1 instead of 0. (Ex: Node 1 will have (1,1) as (x,y) coordinates)
* Below is a sample grid structure that is created with size = 3 and represented as a Python list
```
 [(1, [1, 1]), (2, [1, 2]), (3, [1, 3]), (4, [2, 1]), (5, [2, 2]), (6, [2, 3]), (7, [3, 1]), (8, [3, 2]), (9, [3, 3])]
```
* Once the grid was created with index values and (x,y) coordinates, if we mention the debug value is True, this method will print (x,y,i) features for all the nodes created in grid
* Below method will take index of the node as a parameter and returns (x,y) coordinates of specified node index value
```
 def return_cords(self, index):
```
* Task 1 is developed using python functions and Python Lists. The specific implementation part is mentioned in code as comments

### Task 2 - Finding Neighbors
* Second task is to add a method that will accept either (x,y) or index of the node. It also accepts the radius of neighborhood (m) and the type of neighborhood pattern to return the neighboring nodes that falls in specified pattern. Below is the specified method name
```
 def neighborhood_nodes(self, x, y, i, m ,type):
```
* This method will check if the user has entered either (x,y) or i. If not, it will print the error message. Also, this will check if the entered radius is > 0 and < size/2
* This method will call another method stated below for getting neighbors in preferred patterns
```
 def patterns(self, x, y, m, type)
```
* Task 2 is developed using Python functions and exceptions were handled where ever possible. The algorithm can be found in the code sample and comments were provided for better understanding of code

### Task 3 - SQL Schema
* Assume that this Python application is logging all values to a database that were calculated by different methods stated in the application
* Suppose if we are initializing the NeighboringNodes class with size, assume that value is written to a table named **grid** in MYSQL Database
* The table structure for grid is given below with create table command
```
MYSQL command: CREATE TABLE grid (
  grid_size INT,
  PRIMARY KEY(grid_size));
  INSERT INTO grid (grid_size) VALUES(3), (5), (7);

table grid:

|grid_size (int)|
|---------------|
|       3       |
|       5       |
|       7       |
```
* Once above table was created, assume that a n x n size grid is created and respective (x,y) and index values are stored to **grid_structure** table as below
```
MYSQL command: CREATE TABLE grid_structure (
  size INT,
  x_value INT,
  y_value INT,
  m_index INT,
  FOREIGN KEY(size) REFERENCES grid(grid_size));

table grid_structure:

|   size (int)  |   x_value (int)  |  y_value (int) |   m_index (int) |
|-------------- | -----------------| ---------------|-----------------|
|       3       |        1         |       1        |        1        |
|       3       |        1         |       2        |        2        |
|       3       |        1         |       3        |        3        |
|       3       |        2         |       1        |        4        |
|       3       |        2         |       2        |        5        |
|       3       |        2         |       3        |        6        |
|       3       |        3         |       1        |        7        |
|       3       |        3         |       2        |        8        |
|       3       |        3         |       3        |        9        |
|       5       |        1         |       1        |        1        |
|       5       |        1         |       2        |        2        |
|       .       |        .         |       .        |        .        |
|       .       |        .         |       .        |        .        |
|       .       |        .         |       .        |        .        |
|       .       |        .         |       .        |        .        |
|       7       |        7         |       7        |        49       |
```
* Assume that if we call neighboring_nodes() method, a table called **patterns** with radius, type of pattern and grid size were created as shown below
```
MYSQL command: CREATE TABLE patterns (
  grid_size INT,
  pattern_type VARCHAR(20),
  radius INT,
  FOREIGN KEY(grid_size) REFERENCES grid(grid_size));

table patterns:

|grid_size (int)| pattern_type (varchar) | radius (int) |
|-------------- | -----------------------|--------------|
|       3       |        DIAMOND         |      1       |
|       5       |        CROSS           |      2       |
|       3       |        SQUARE          |      1       |
|       7       |        DIAMOND         |      3       |
```
* Since we have created three tables, we have foreign key relations between tables. **patterns** and **grid_structure** tables were related to **grid**. Referential integrity is defined below
```
 -> grid_size key is the PRIMARY KEY for grid
 -> size key in grid_structure is a FOREIGN KEY for grid
 -> grid_size key in patterns is a FOREIGN KEY for grid
```
#### SQL Examples
* Consider for example, we want to calculate the total radius measured for each grid and display output in descending order of total. This value can be calculated by the below SQL command
```
select grid_size, sum(radius) as tot_radius from patterns
GROUP BY grid_size
ORDER BY tot_radius desc;
```
* Consider that we need x and y coordinate values at index = 5 for pattern type = DIAMOND and grid size = 5. This can be acheived by the below SQL command
```
with grid_values as (select g.grid_size as size, gs.x_value, gs.y_value from grid g
  JOIN grid_structure gs
  on g.grid_size = gs.size)
select gv.x_value, gv.y_value, p.pattern_type from patterns p
JOIN grid_values gv
on p.grid_size = gv.size
WHERE gv.size = 5 and p.pattern_type = "DIAMOND";
```
## Prerequisites
This Algorithm is built by using Python 3.7.6 and need a Python environment to run the code and pass different parameters for desired output

## Defining Parameters
* Both Task 1 and Task 2 require some parameters to be passed to get the desired result
* If we want to initiate a grid with size = 7 and debug = False, this can be done in the code snippet by passing parameters as below
```
object = NeighboringNodes(7, False)
object.create_grid()
```
* If we want to print the coordinates for node having index = 12, this is achieved by passing parameter as mentioned below
```
coordinates = object.return_cords(12)
print(coordinates)
```
* If we want to get the neighboring nodes for the node having (4,4) coordinates, radius = 2 and pattern type = DIAMOND, parameters must be passed as mentioned below
```
neighbor_nodes = object.neighborhood_nodes(x = 4, y = 4, i = None , m = 2, type = "DIAMOND")
print(neighbor_nodes)
```
* Remember to specify either (x,y) or i. If (x,y) is passed, i has to be None as mentioned and if i is passed, (x,y) has to be None

## Running Tests
* Fork this repository to the local computer or just download challenge.py file form the repository
* Open any code editor and pass the parameters based on desired output
* Open command prompt, navigate to the repository where challenge.py file is stored and execute below command
```
python challenge.py
```
