# MESA - Getting Started with Boltzmann 

This is an implementation of the [Introductory Tutorial](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html) at the Mesa website. The tutorial implements the simple and powerful Boltzmann model, while demonstrating the major features of the Mesa and showcases the model's counterintuitive distributive outcomes. We implement the [Batch Run](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html#batch-run) which allows insight to be developed though varying the starting parameters and comparing aggregated metrics. 

## Installation
This installation routine, and the display of the charts, was tested on a Windows machine running VS Code connecting over SSH to a linux machine. If you have a difficultly with a different configuration or have a question [please let me know](mailto:matt.mcgee@ucdconnect.ie).

We use the package manager [pip](https://pip.pypa.io/en/stable/) to install Mesa.

## Setup
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

## Windows Charts

So far, if everything worked ok, we can see basic console output summarising multiple runs of agents and models. Don't worry if it's hard to intertpret, the charts can be generated in VS Code on Windows as by adding the [Jupyter](https://jupyter.org/) extension and clicking on Run Above in either run.py or batch.py.


![Run Charts](https://github.com/vinylmatt/boltzmann_example/blob/master/RunCharts.gif?raw=true)

## Batches

Batches are very useful for running sets of tests and varying  parameters. See the comments in the code for more information to see the Batch Run Charts

![Run Charts](https://github.com/vinylmatt/boltzmann_example/blob/master/RunChartsBatch1.gif?raw=true)

## Experience
The [Introductory Tutorial](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html) is well paced, introducing major topics in a way that requires that the student contextualise with the previous steps - enhancing understanding. 

At the same time, the steps give ways of developing insight into the model; when there is only a time dimention it was difficult to believe it was working, but when space is introduced into the model, it becomes possible to make small populations and big grids.

## Additional Material

The MESA examples also included many oven-ready scripts, the project folder also contains an implementation of one of these, see the [example code on GitHub](https://github.com/projectmesa/mesa/tree/main/examples/wolf_sheep). In our implementation, we added an extra layer of predation where an onmivorous shepherd can prey on wolves, sheep and eat grass, depending on need. 

The sample code has a more advanced presentation layer, and was fun to play with, the better presentation layer made the model more usable (and fun to play with) - I focussed on trying to get the populations of the 3 different mammals to last as many 'ticks' as possible. It is easy to see, in hindside, where the Batch Runner in the Introductory Tutorial would have helped.

## Open the Additional Material
```bash
# Open the Predation Model
mesa runserver additional_material

```

## More Additional Material

While exploring the topic before the project specification was released I had a look the
'Modelling for All' tool referenced in the . This is run on the Windows PC using NetLogo or in the browser. This had a drag and drop interface and it was possible to do an impolmentation of the 2 predator - prey model with an aversion to the proximity of shepherds, using the same technique in the Schelling model.

## Modelling for all Training Material

A [tutorial](https://www.youtube.com/watch?v=HALiXCTaoMk&t=2s&ab_channel=KenKahn) on the platform from the tool author offered a blank slate implementation of Thomas Schelling’s Segregation Model, comparable in approach to that of MESA.

## Extending the model with an extra predator

Version 1 with 2 simple predators (no avoidance)
http://m.modelling4all.org/m/?frozen=-swtA0uulUxYgny1cIP57c&MforAllModel=1

## Smarter Intermediate Predator

Version 2 with 1 simple predator and 1 smart wolf
http://m.modelling4all.org/m/?frozen=bKHpqKSuhhWfNuitI14548&MforAllModel=1

Either of the above models can be run in the browser or downloaded to the and run with a local copy of NetLogo on the PC.

## Thoughts

Testing setup from observation 22 runs in this environment, avoidant wolf populations endured 10% longer on average. Further observation is required to assess this strategy’s effectiveness, and the batch run feature of MESA would have been useful here to develop more confidence in the model's function. One standout feature of this tool was how easy it was to build complexity in the modelling language and how easy the models are to share.
