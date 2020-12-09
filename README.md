# Multi-Vehicle-Routing
Course project for 16.413/6.877- Principles of Autonomy and Decision Making, Fall 2020

## Usage:
Open [`mvrp.ipynb`](https://github.com/nsidn98/Multi-Vehicle-Routing/blob/main/mvrp.ipynb) for the final draft of the project.

References are listed in the [`docs/`](https://github.com/nsidn98/Multi-Vehicle-Routing/tree/main/docs) folder. 

## Minizinc test file:
Run `python minizinc_test.py` to get the following output:
```
##################################################
Number of customers are: 8
Demands at each node are: [10, 5, 16, 1, 18, 28, 29, 0]
Number of vehicles available: 10
Maximum capacity of each vehicle: 30
##################################################

########## SOLUTION FOUND ####################
Distance Travelled: 507
Number of Vehicles used: 4
##################################################
```
![Example solution](https://raw.githubusercontent.com/nsidn98/Multi-Vehicle-Routing/main/assets/vrp_solution.png?token=AGFGCMCK5U6W6DSUFBIV5YS73JR4Q)
