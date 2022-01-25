from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from wolf_sheep.agents import Wolf, Sheep, Shepherd, GrassPatch
from wolf_sheep.model import WolfSheep


def wolf_sheep_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Sheep:
        portrayal["Shape"] = "wolf_sheep/resources/sheep.png"
        # https://icons8.com/web-app/433/sheep
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is Wolf:
        portrayal["Shape"] = "wolf_sheep/resources/wolf.png"
        # https://icons8.com/web-app/36821/German-Shepherd
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"

    elif type(agent) is Shepherd:
        portrayal["Shape"] = "wolf_sheep/resources/man.png"
        # https://img.icons8.com/external-itim2101-fill-itim2101/344/external-man-avatar-itim2101-fill-itim2101.png
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["text"] = round(agent.energy, 1)
        portrayal["text_color"] = "White"    

    elif type(agent) is GrassPatch:
        if agent.fully_grown:
            portrayal["Color"] = ["#95bf95", "#8cc28c", "#82c282"]
        else:
            portrayal["Color"] = ["#ffffff", "#ffffff", "#ffffff"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal


canvas_element = CanvasGrid(wolf_sheep_portrayal, 20, 20, 500, 500)
chart_element = ChartModule(
    [{"Label": "Shepherds", "Color": "#786956"}, {"Label": "Wolves", "Color": "#548282"}, {"Label": "Sheep", "Color": "#a4caca"}]
)

model_params = {
    "grass": UserSettableParameter("checkbox", "Grass Enabled", True),

        "initial_shepards": UserSettableParameter(
        "slider", "Initial Shepherd Population", 2, 0, 300
    ),

        "initial_wolves": UserSettableParameter(
        "slider", "Initial Wolf Population", 10, 0, 300
    ),

        "initial_sheep": UserSettableParameter(
        "slider", "Initial Sheep Population", 100, 0, 300
    ),
        "shepherd_gain_from_food": UserSettableParameter(
        "slider", "Shepherd Gain From Sheep Rate", 20, 1, 50
    ),
        "shepherd_gain_from_grass": UserSettableParameter(
        "slider", "Shepherd Gain From Grass Rate", 20, 1, 50
    ),
        "wolf_gain_from_food": UserSettableParameter(
        "slider", "Wolf Gain From Food Rate", 20, 1, 50
    ),

        "sheep_gain_from_food": UserSettableParameter(
        "slider", "Sheep Gain From Food Rate", 20, 1, 50
    ),


    "grass_regrowth_time": UserSettableParameter(
        "slider", "Grass Regrowth Time", 20, 1, 50
    ),

    "shepherd_reproduce": UserSettableParameter(
        "slider",
        "Shepherd Reproduction Rate",
        0.05,
        0.00,
        1.0,
        0.01,
        description="The rate at which Shepherd agents reproduce.",
    ),

    "wolf_reproduce": UserSettableParameter(
        "slider",
        "Wolf Reproduction Rate",
        0.05,
        0.01,
        1.0,
        0.01,
        description="The rate at which wolf agents reproduce.",
    ),

    "sheep_reproduce": UserSettableParameter(
        "slider", "Sheep Reproduction Rate", 0.04, 0.01, 1.0, 0.01
    ),








    
    




    "sheep_gain_from_food": UserSettableParameter(
        "slider", "Sheep Gain From Food", 4, 1, 10
    ),
}

server = ModularServer(
    WolfSheep, [canvas_element, chart_element], "Wolf Sheep Predation", model_params
)
server.port = 8521
