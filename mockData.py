from random import random

def get_values(numVals):
    points = []
    scaler = random()
    exactPos = {"x": 10*random(), "y": 10*random(), "z": 10*random()}
    for i in range(numVals):
        gps = {"x": 10*random(), "y": 10*random(), "z": 10*random()}
        signal = (1 + random()*0.01) * scaler * ((gps["x"] - exactPos["x"])**2 + (gps["y"] - exactPos["y"])**2 + (gps["z"] - exactPos["z"])**2)**0.5
        gps["signal"] = signal
        points.append(gps)
    return points, exactPos
