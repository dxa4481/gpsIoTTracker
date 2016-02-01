# gpsIoTTracker
This simple python module takes GPS locations of a moving object, and measured signal strengths of an IoT object and uses trilateration and the method of least squares to solve for the location of the object 

## How to use

First import the solving funciton

```python
from solver import get_device_location
```

Pass the solver function all the measured points and signal strengths as follows

```python
get_device_location([{"x": 1, "y": 4, "z": 1.6, "signal": 1.3}, {"x": 3, "y": 3.5, "z": 7.5, "signal": 3.3}...]
```

## Results

The function will return values of the form
```python
{"x": 1, "y": 4, "z": 1.6, "sigPower": 1.3}
```
where x, y, and z are the coordinates of the IoT object, and sigPower is a scaler you can multiply the signal strength by to get the distance away the object is
