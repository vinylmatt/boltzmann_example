from bleach import clean
from money_model import MoneyModel
import matplotlib.pyplot as plthist
import matplotlib.pyplot as plt1
import numpy as np

# %%
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
    return (1 + (1/N) - 2*B)

# %%

agent_wealth = []
# %%
for j in range(100):
    # Run the model
    model = MoneyModel(10, 4, 4)
    # test this works ok by doing
    # model = MoneyModel(4, 100, 100) and looking at chartby run over a range of 1
    # if it's working, it's often 1

    for i in range(100):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        agent_wealth.append(agent.wealth)

plthist.hist(agent_wealth, bins=range(max(agent_wealth)+1))
# %%
#heatmap of locations and cash
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt1.imshow(agent_counts, interpolation='nearest')
plt1.colorbar()
plthist.colorbar()

# %%

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
# %%

# %%
agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.head()
# %%

end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max() + 1))

# %%
one_agent_wealth = agent_wealth.xs(2, level="AgentID")
one_agent_wealth.Wealth.plot()

# %%
