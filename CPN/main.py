import turtle as t
from tkinter import *
from tkinter import filedialog
import random as r
from PIL import Image, ImageTk
import colorgram
import os, sys


# User will locate Img they and and create a Pillow Object from it to use in ColorGram.py

def locateImg():
    imgFinder = filedialog.askopenfilename(title = "select Image File", fileTypes = (('JPG file', "*.jpg"), ("PNG file", '.*.png')), intialdir = os.getcwd())
    

# Main User Interface

root = Tk()
root.title('Hello Artist')
root.geometry("1000x1000")

# Image color extraction: I commented it out to save memory on our computers.
# User would input the number of colors they want from the image:
# Ex. They pick 20.


extractedColors = colorgram.extract('test.png', 20)
colorList = []  # can uncomment and mess around with it.
for color in extractedColors:
    newColor = (color.rgb.r, color.rgb.g, color.rgb.b)
    colorList.append(newColor)

# print(colorList)

t.colormode(255)

# Sample color list made from above.

# turtle program to run colors

screen = t.Screen()
screen.title("Color Palette Generator")
generator = t.Turtle()
generator.shape("arrow")
generator.hideTurtle()
generator.speed("fastest")
generator.penup()
generator.setheading(135)
generator.forward(375)
generator.setheading(0)

numOfColors = len(colorList)

for dot in range(1, numOfColors):
    color = colorList[dot - 1]
    generator.dot(50, color)
    generator.forward(50)
    if dot % 10 == 0:
        generator.setheading(270)
        generator.forward(50)
        generator.setheading(180)
        generator.forward(500)
        generator.setheading(0)

# canvas saving features. Currently saves as a .eps file (which can be opened with Preview as a PDF) but working on
# converting the .eps file to a universal .png or .jpg file
# Requires installing ghostscript (using 'pip install' gave me errors, so i used homebrew to install the package)
screenCapture = generator.getscreen()  # hs = captures the screen of the 'generator', to be used later for exporting the pallet
screenCapture.getcanvas().postscript(file="out.eps")  # hs = exports the screenCapture as a eps file (typescript)
outputFile = "output_result.png"  # hs = name of output file of final .png output file
Image.open("out.eps").convert('RGBA').save(outputFile, lossless=True)  # hs = converts eps file to RGBA(.png) color profile and saves as .png

# deletes the .eps file HOWEVER .eps seems to be higher quality than the .png (up to you if you want to keep
# the .eps file)
# os.remove("out.eps")  # hs = removes 'out.eps' from system

# Option to save the image

screen.exitonclick()
