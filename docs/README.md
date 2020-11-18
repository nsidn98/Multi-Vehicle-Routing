[INTRODUCTION AND BACKGROUND](https://docs.google.com/document/d/1erjKy4EParSTpvh_4yV5FFI5dJq7n7SsHHq6Mrpjaww/edit)

## Multi-Vehicle Routing

In this task, you will assign the order in which workstations are visited by your fleet of droids. You will
be given the locations of a set of workstations which must be visited and your current location. For each
droid, you must assign the order in which they visit a subset of the workstations before returning to your
location. You will be asked to find the minimum time plan, such that each workstation is visited by at
least one droid.

### Achieving task using constraint optimization
Inputs:
1) Location of depot
2) Goal locations
3) Travel times between locations

Outputs:
1) Sequence of location(s) for each agent
 
### Readings and course lectures for constraint programming:
* L12 Constraint Programming
    * Constraint modelling applied to visual interpretation and scheduling; arc consistency, constraint propagation, AC-1 and AC-3. 
    * Reading: [AIMA] Chapters 6.1, and 24.3-5. 
    * Optional reading [CP] Ch 2.
 
* L13 Solving Constraint Programs – Propagation and Basic Search
    * Constraint propagation, consistency, and basic search. 
    * Reading: [AIMA] Chapter 6.2. 
    * Optional reading [CP] Ch 3.con
 
* L14 Solving Constraint Programs – Forward Checking and Elimination
    * Backtrack search, BT with forward checking. dynamic variable ordering and iterative repair. 
    * Reading: [AIMA]
    * Chapter 6.3-5. Optional reading [CP] Ch 5, 6 and 7.


* [AIMA] “Artificial Intelligence: A Modern Approach,” by Russell and Norvig.
* [CP] “Constraint Processing,” by Rina Dechter (Morgan Kaufmann).

### Papers/slides related to Constraint Optimization for Multi-Vehicle Routing Problem
* [Solving Vehicle Routing Problems using Constraint Programming and Metaheuristic](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.8686&rep=rep1&type=pdf) by Backer et al.
* [Constraint-based solution methods for vehicle routing problems](http://egon.cheme.cmu.edu/ewo/docs/EWO_seminar_van_Hoeve.pdf) by Hoeve.
* [Multi-Vehicle Routing](http://web.stanford.edu/~pavone/papers/Frazzoli.Pavone.ESC13.pdf) by Frazzoli and Pavone.
* [Reinforcement Learning for Solving the
Vehicle Routing Problem](https://papers.nips.cc/paper/8190-reinforcement-learning-for-solving-the-vehicle-routing-problem.pdf) by Nazari et al.
* [Benchmark Dataset](http://web.cba.neu.edu/~msolomon/problems.htm) for Vehicle Routing Problem by Solomon.
* [Method](http://mistic.heig-vd.ch/taillard/articles.dir/GoldenLT1997.pdf) for solving multi-vehicle problem by Golden et al.


