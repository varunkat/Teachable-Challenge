# Neighboring Nodes Challenge

The below challenge is focused on constructing a nxn grid of defined size n consisting of (x,y) coordinates and index in the order of grid creation. Users can specify different parameters to know the coordinates, index position and print out patterns (SQUARE, CROSS and DIAMOND) based on their requirements. A Database schema was designed leveraging different tables and assumptions and was discussed in detail in the below sections.


## Development

This challenge was divided into three tasks and the detailed description for each task is provided below.

###Task 1 - Build the grid
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
* Once the grid was created with index values and (x,y) coordinates, if we mention the debug value is True, this method will print (x,y,i) features for all the nodes created in grid.
* Below method will take index of the node as a parameter and returns (x,y) coordinates of specified node index value.
```
 def return_cords(self, index):
```
* Task 1 is developed using python functions and Python Lists. The specific implementation part is mentioned in code as comments


## Prerequisites
This Algorithm is built by using Python 3.7.6 and need a Python environment to run the code and pass different parameters for desired output.

### Installing



## Running the tests
