from bleach import clean
from money_model import MoneyModel
import matplotlib.pyplot as plt
import numpy as np
# %%

agent_wealth = []

for j in range(10):
    # Run the model
    model = MoneyModel(100)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        agent_wealth.append(agent.wealth)
clean
plt.hist(agent_wealth, bins=range(max(agent_wealth)+1))
# %%
# %%

# %%
