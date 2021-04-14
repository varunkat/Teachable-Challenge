# NEIGHBORING NODES CHALLENGE

The below challenge is focused on constructing a nxn grid of defined size n consisting of (x,y) coordinates and index in the order of grid creation. Users can specify different parameters to know the coordinates, index position and print out patterns (SQUARE, CROSS and DIAMOND) based on their requirements. A Database schema was designed leveraging different tables and assumptions and was discussed in detail in the below sections.


## Development

This challenge was divided into three tasks and the detailed description for each task is provided below.

### Task 1 - Build the grid
* First task is about building a class that will accept two different parameters (size, debug) and adding methods to construct the grid and another method to return coordinates of the index
* The name of the class is mentioned below
```
class NeighboringNodes():

    def __init__(self, size, debug:bool):
```
* After the class is initiated, below method will create size X size grid with (x,y) coordinates and index values in the order of grid creation
```
 def create_grid(self):
```
* This algorithm was designed to assign coordinates from 1 instead of 0. (Ex: Node 1 will have (1,1) as (x,y) coordinates)
* Below is a sample grid that is created with size = 3
```
 [(1, [1, 1]), (2, [1, 2]), (3, [1, 3]), (4, [2, 1]), (5, [2, 2]), (6, [2, 3]), (7, [3, 1]), (8, [3, 2]), (9, [3, 3])]
```
* Once the grid was created with index values and (x,y) coordinates, if we mention the debug value is True, this method will print (x,y,i) features for all the nodes created in grid.
* Below method will take index of the node as a parameter and returns (x,y) coordinates of specified node index value.
```
 def return_cords(self, index):
```
* Task 1 is developed using python functions and Python Lists. The specific implementation part is mentioned in code as comments

### Task 2 - Finding neighbors
* Second task is to add a method that will accept either (x,y) or index of the node. It also accepts the radius of neighborhood (m) and the type of neighborhood pattern to return the neighboring nodes that falls in specified pattern. Below is the specified method name.
```
 def neighborhood_nodes(self, x, y, i, m ,type):
```
* This method will check if the user has entered either (x,y) or i. If not, it will print the error message. Also, this will check if the entered radius is > 0 and < size/2.
* This method will call another method stated below for getting neighbors in preferred patterns
```
 def patterns(self, x, y, m, type)
```
* Task 2 is developed using Python functions and exceptions were handles where ever possible. The algorithm can be found in the code sample and comments were provided for better understanding of code.

### Task 3 - SQL schema
* Assume that this Python application is logging all values to a database that were calculated by different methods stated in the application.
* Suppose if we are initializing the NeighboringNodes class with size and debug value, those values are written to a table named grid_operations in MYSQL Database
* The table structure for grid_operations is given below.
```
|grid_size (int)| debug (boolean) |
|-------------- | ----------------|
|       3       |      True       |
|       5       |      True       |
|       3       |      False      |
|       7       |      False      |
```

## Prerequisites
This Algorithm is built by using Python 3.7.6 and need a Python environment to run the code and pass different parameters for desired output.

## Running tests
*
