# Connected Sinks
Given a text file with entries of a pipe system, the program will determine which sinks are connected to the source.

### Details
The program processes the file data, creates a graph, and collect the row and column position of the source (denoted by the * symbol). It then calls a helper function to run the depth-first search algorithm starting at the source and stores all found sinks, which takes in several parametesrs including the graph, row, and column that were obtained earlier. Lastly, all the founded sinks are sorted in alphabetical order and returned as a string.

For the sample pipe system below:
```
* ╣ ╔═ A
  ╠═╝
  C ╚═ B
```

The output will be: `AC`

## How to Run
1) Execute the program with `py connected_sinks.py`
    * Install Python [here](https://www.python.org/downloads/)