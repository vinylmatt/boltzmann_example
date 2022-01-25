from bleach import clean
from money_model import MoneyModel
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from mesa.batchrunner import BatchRunner
import pandas as pd
import numpy as np

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
    return (1 + (1/N) - 2*B)

fixed_params = {"width": 10,
               "height": 10}
variable_params = {"N": range(10, 500, 10)}
#variable_params = {"N": range(10, 500, 10)}
#The total number of runs is 245. 
# That is 10 agents to 490 increasing by 10, 
# making 49 agents populations. 
# Each agent population is then run 5 times 
# (n of agent * 5) for 245 iterations

#Faster
#variable_params = {"N": range(10, 100, 10)}
# The total number of runs is 45. 
# That is 10 agents to 90 increasing by 10, 
# making 9 agents populations. 
# Each agent population is then run 5 times 
# (n of agent * 5) for 45 iterations

batch_run = BatchRunner(MoneyModel,
                        variable_params,
                        fixed_params,
                        # Each agent population is  run 5 times
                        iterations=5,
                        max_steps=100,
                        model_reporters={"Gini": compute_gini})

                        
batch_run.run_all()
# %%
run_data = batch_run.get_model_vars_dataframe()
run_data.head()
# %%
plt.scatter(run_data.N, run_data.Gini)
# %%

#Get the Agent DataCollection
data_collector_agents = batch_run.get_collector_agents()
values = data_collector_agents.values()
print(values)

#Get the Model DataCollection.

data_collector_model = batch_run.get_collector_model()
values = data_collector_model.values()
print(values)
# %%


