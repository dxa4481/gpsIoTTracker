from mockData import get_values
from numpy import matrix
from numpy.linalg import lstsq


def get_device_location(gpsPoints):
    """
        params: takes an array of gps positions and signal stregnths of the form [{"x": 1, "y": 4, "z": 1.6, "signal": 1.3}]
        returns: Position and output power of emitter of the form {"x": 1, "y": 4, "z": 1.6, "sigPower": 1.3}
    """
    aRows = []
    bRows = []
    last = gpsPoints.pop()
    for gpsPoint in gpsPoints:
        aRow = [2.0 * (last["x"] - gpsPoint["x"]),
                2.0 * (last["y"] - gpsPoint["y"]),
                2.0 * (last["z"] - gpsPoint["z"]),
                (-1 * gpsPoint["signal"]**2 + last["signal"]**2)]
        bRow = [-(gpsPoint["x"]**2 - last["x"]**2)  - (gpsPoint["y"]**2 - last["y"]**2) - (gpsPoint["z"]**2 - last["z"]**2)]
        aRows.append(aRow)
        bRows.append(bRow)
    aMatrix = matrix(aRows)
    bMatrix = matrix(bRows)
    solution = lstsq(aMatrix, bMatrix)[0]
    return {"x": solution.item(0), "y": solution.item(1), "z": solution.item(2), "sigPower": solution.item(3)}


gpsPoints, exactPos = get_values(7)

print get_device_location(gpsPoints)
