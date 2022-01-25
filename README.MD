# MESA - Getting Started with Boltzmann 

This is an implementation of the [Introductory Tutorial](https://mesa.readthedocs.io/en/master/tutorials/intro_tutorial.html) at the Mesa website. The tutorial implements the simple and powerful Boltzmann model, while demonstratings the major features of the Mesa and showcases the models counter intutitive distruibitive outcomes. Finally we implement the BatchRunner which allows insights to be developed though varying the staring paramenters and comparing aggregated metrics. 

## Prerequistes 

## Installation
This installation routine, and the display of the charts, was tested on a Windows machine running VS Code connecting over SSH to a LAMP stack Linux box. If you find an error bug or have a question [please let me know](mailto:matt.mcgee@ucdconnect.ie).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Mesa.

```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python-numpy
pip install mesa
# install dependencies
pip install -r https://raw.githubusercontent.com/projectmesa/mesa/master/examples/boltzmann_wealth_model/requirements.txt

pip install -r jupyter
pip install -r  matplotlib
pip install -r  install mesa
pip install -r  install numpy
sudo snap install gh
cd /your/path/boltzmann_example

```

## For Windows Visualisation

The path must be added

```python
export PATH=/home/matt/.local/bin:$PATH

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)




```python
export PATH=/home/matt/.local/bin:$PATH

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```