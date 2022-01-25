from bleach import clean
from money_model import MoneyModel
import matplotlib.pyplot as plthist
import matplotlib.pyplot as plt1
import numpy as np

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
    return (1 + (1/N) - 2*B)



agent_wealth = []
for j in range(100):
    # Run the model with 50 agents in a 10x10 grid
    model = MoneyModel(50, 10, 10)
    # some surprising results, but if we make the agents 
    # hermits that never meet, they hang onto their cash
    # we can see this with parameters
    # model = MoneyModel(4, 100, 100) 
    # and looking at chartby run over a range of 1
    # if it's working, it's often 1

    #test with 100 runs
    for i in range(100):
    
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        agent_wealth.append(agent.wealth)

# %%
#Display the distribution of wealth on a histogram
plthist.hist(agent_wealth, bins=range(max(agent_wealth)+1))
# Click 'Run Above' in VS Code to display this histogram
# %%

#heatmap of agent locations and their cash
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt1.imshow(agent_counts, interpolation='nearest')
plt1.colorbar()
plthist.colorbar()
# %%

# Gini Coefficient of all the runs
gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
# %%

# %%
agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.head()
# %%
#Agent wealth at model end (runs 0 - 99)
end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max() + 1))
# %%

#The cash level over the steps of agent
one_agent_wealth = agent_wealth.xs(2, level="AgentID")
one_agent_wealth.Wealth.plot()

# %%
