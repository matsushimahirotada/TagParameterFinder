import numpy as np
import math

def exposuretiming(freq,dptr,dptrmax):
    
    Ts = 1/freq
    theta = math.asin(dptr/dptrmax)
    theta2 = math.pi - theta 
    t1=(Ts*theta)/(2*math.pi)
    t2=(Ts*theta2)/(2*math.pi)
    Time = [t1,t2]
    
    return Time    
