# Multi-Vehicle-Routing
Multi Vehicle Routing. (16.413/6.877- Principles of Autonomy and Decision Making course project)

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
![Example solution](https://raw.githubusercontent.com/nsidn98/Multi-Vehicle-Routing/main/assets/vrp_solution.png?token=AGFGCMD6SSEPI4KSKJBRKGK7X2UGO)
## Google Colaboratory Support
Open the notebook in Google Colaboratory:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nsidn98/Multi-Vehicle-Routing/blob/main/multi-vehicle-routing.ipynb)

## Instructions for setting up colab: 
### Setup:
Once you click on the link, it lead you to a page where it will state that `Notebook not found`. At this point click on `Authorise with GitHub` which will ask you for your Github username and password. Even after filling this, you might get a pop-up stating `Notebook not found`. Click on `OK` and then click on `Include private repos` in the new pop-up. After this scroll down over the `Repository` tab and choose `nsidn98/Multi-Vehicle-Routing` at which point you will see the `multi-vehicle-routing.ipynb` notebook.

### Saving changes:
Once you make the changes in the colab notebook you have to push the changes in the repository. For this, click on `File` and then `Save a copy in GitHub` and then add the commit message (one line stating the major changes in the file) and click on `OK`