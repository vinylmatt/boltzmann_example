from bleach import clean
from money_model import MoneyModel
import matplotlib.pyplot as plthist
import matplotlib.pyplot as plt1
import numpy as np
# %%

agent_wealth = []

for j in range(100):
    # Run the model
    model = MoneyModel(100, 50, 50)
    # test this works ok by doing
    # model = MoneyModel(4, 100, 100) and looking at chartby run wover a range of 1
    # if it's working, it's often 1

    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        agent_wealth.append(agent.wealth)

plthist.hist(agent_wealth, bins=range(max(agent_wealth)+1))
# %%
# %%
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt1.imshow(agent_counts, interpolation='nearest')
plt1.colorbar()
plthist.colorbar()

# %%
# %%

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
# %%