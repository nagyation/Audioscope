import numpy as np
import matplotlib.pyplot as plt

class SignalPlotter:


    def __init__(self,timeStep,timeMax):
        """
        timeStep : the step for time Axis from second
        timeMax : the max time in the time Axis in same scale
        
        """
        self.time = []
        self.amp = []
        self.timeStep = timeStep
        self.timeMax = timeMax
        self.numberOfSteps = timeMax/timeStep
        plt.plot(self.time,self.amp)
        plt.ion()
        self.time.append(0) #the base to increment over it
       

    #manages signal relative to time
    def __manageSignal(self):
        if len(self.amp) > self.numberOfSteps:
            del self.amp[0] #shift signal by deleting the first element
        if len(self.time) != self.numberOfSteps and len(self.time) < len(self.amp):
            self.time.append(self.time[-1]+self.timeStep)
            
    def addAmp(self,amp):
        self.amp.append(amp)
        self.__manageSignal()

    def draw(self):
        plt.gca().lines[0].set_xdata(self.time);
        plt.gca().lines[0].set_ydata(self.amp);
        plt.gca().relim();
        plt.gca().autoscale_view();
        plt.pause(self.timeStep)


p = SignalPlotter(0.001,0.2)
#y.append(2*np.sin(2 * np.pi * i))
points = []
count = 0.0
while True:
    count += 0.2
    points.append(count)
    if len(points) == 1000:
        break

i = 0
while True:
    
    y = 2 * np.sin( np.pi *points[i]) 
    p.addAmp(y)
    p.draw()
    i = (i+1)%len(points)
