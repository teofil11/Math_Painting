import numpy as np
from PIL import Image

class Canvas():

    def __init__(self, height, width,color):
        self.height = height
        self.width = width
        self.color = color

        #Create a 3d numpy arrayof zeros
        self.data = np.zeros((self.height, self.width, 3), dtype = np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img =Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle():

    def __init__(self, height, width, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, canvas):
        # Draw the rectangle into the canvas
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square():

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        # Draw the square into the canvas
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
