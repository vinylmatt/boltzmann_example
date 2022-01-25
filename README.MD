# MESA - Getting Started with Boltzmann 

This is an implementation of the [Introductory Tutorial](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html) at the Mesa website. The tutorial implements the simple and powerful Boltzmann model, while demonstrating the major features of the Mesa and showcases the model's counter intuitive distributive outcomes. We implement the BatchRunner which allows insight to be developed though varying the starting parameters and comparing aggregated metrics. 

## Installation
This installation routine, and the display of the charts, was tested on a Windows machine running VS Code connecting over SSH to a linux machine. If you have a difficultly with a different configuration or have a question [please let me know](mailto:matt.mcgee@ucdconnect.ie).

We use the package manager [pip](https://pip.pypa.io/en/stable/) to install Mesa.

```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python-numpy
pip install mesa
# install dependencies
pip install -r https://raw.githubusercontent.com/vinylmatt/boltzmann_example/master/requirements.txt
sudo snap install gh
# Open this folder in terminal
cd /your/path/boltzmann_example
# Check everything is working by running the batch runner. This takes a while.
python3 batch.py


```

## For Windows Visualisation

So far, if everything worked ok, we can see basic console output summarising multiple runs of agents and models. Don't worry if it's hard to intertpret, the charts can be generated in VS Code on Windows as by adding the [Jupyter](https://jupyter.org/) extension and clicking on Run Above in either run.py or  batchrunner.py.


//gif console output

## Experience
The [Introductory Tutorial](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html) is well paced, introducing major topics in a way that requires that the student contextualise with the previous steps - enhancing understanding. 

At the same time, the steps give ways of developing insight into the model; when there is only a time dimention it was difficult to believe it was working, but when space is introduced into the model, it becomes possible to make small populations and big grids.

## Future Improvements
Add chart labels
Advanced tutorial for javascript implemention of visualisation  
Experiment with toroidal grid

## Additional Material

The MESA examples also included many oven ready scripts, the project folder also contains an implementation of one of these, see the [example code on GitHub](https://github.com/projectmesa/mesa/tree/main/examples/wolf_sheep). In our implementation, we added an extra layer of predation where an onmivorous shepherd can prey on wolves, sheep and eat grass, depending on need. 

The sample code has a more advanced presentation layer, and was fun to play with, the better presentation layer made the model more usable (and fun to play with) - I focussed on trying to get the populations of the 3 different mammals to last as many 'ticks' as possible. It is easy to see, in hindside, where the Batch Runner in the Introductory Tutorial would have helped.


```bash
# Open the Predation Model
mesa runserver additional_material


```




