import turtle as t
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import colorgram
import os, sys

#Methods
def popUp():
    global pop
    pop = Toplevel(root)
    popLabel = Label(pop, text="Type in the Number of Colors from 1 to 30")
    popLabel.pack()
    global popEntry
    popEntry = Entry(pop)
    popEntry.pack()
    popButton = Button(pop, text='Rock n Roll', command=clear)
    popButton.pack()


def extractColors(numberOfColors):
    img = (locateImg())
    extractedColors = colorgram.extract(img, numberOfColors + 1)
    colorList = []  # can uncomment and mess around with it.
    for color in extractedColors:
        newColor = (color.rgb.r, color.rgb.g, color.rgb.b)
        colorList.append(newColor)
    return colorList

def clear():
    numberOfColors = (int)(popEntry.get())
    if numberOfColors > 30 or numberOfColors < 1:
        messagebox.showerror("Title", "Invalid Input")
    else:
        pop.destroy()
        pressedTurtle(numberOfColors)


def locateImg():
    img = filedialog.askopenfilename()
    return img


def pressedTurtle(numberOfColors):
    colorList = extractColors(numberOfColors)
    generator = t.Turtle()
    screen = t.Screen()
    generator.shape("circle")
    generator.hideturtle()
    generator.speed("fastest")
    generator.penup()
    generator.setheading(135)
    numOfColors = len(colorList)
    generator.forward(375)
    generator.setheading(0)
    t.colormode(255)
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
    saveImage(generator)
    screen.exitonclick()
    turtle.bye()

def saveImage(generator):
    screenCapture = generator.getscreen()
    screenCapture.getcanvas().postscript(file="out.eps")
    outputFile = "output_result.png"
    Image.open("out.eps").convert('RGBA').save(outputFile, lossless=True)
    os.remove("out.eps")


#Main
root = Tk()
root.title("Color Palette Generator")
root.geometry("640x400")
root.config(bg = "maroon")

#image
path = ""
canvas = Canvas(root, width= 300, height= 300)
canvas.grid(row=0, pady=15, columnspan= 10)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("color-pencil-1022033_640.jpg"))
canvas.create_image(0,0,anchor=NW, image=img)

#Buttons:
style = ttk.Style()
style.configure('TButton', padding=6, relief="flat", foreground="black", font='georgia 13 bold')
imageLocation = ttk.Button(root, text="Import Image", style='TButton', command=popUp)
savePalette = ttk.Button(root, text="Save Palette")

imageLocation.place(anchor='center', relx=.5, rely=.85)
savePalette.place(anchor='center', relx=.5, rely = .95)

root.mainloop()
