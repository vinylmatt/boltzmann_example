from mesa import Agent, Model
from mesa.time import RandomActivation

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
        print ("Hi, I am agent " + str(self.unique_id) +". My wealth is " + str(self.wealth) +".")       


    def step(self):
        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -= 1
        print ("agent " + str(self.unique_id) +". gave to " + str(other_agent.unique_id) +". My wealth is " + str(self.wealth) +".")       

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)



    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()

