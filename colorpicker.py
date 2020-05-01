'''
James Volino
colorpicker.py

allows the user to pick a color

'''
from breezypythongui import EasyFrame
#Import the tkinter color chooser
import tkinter.colorchooser

class ColorPicker(EasyFrame):
#Displays the results of picking the color

    def __init__(self):
    #Sets up the window, widgets and data
        EasyFrame.__init__(self, title = "Color Picker Demo")
        
        #Labels and outputs fields
        self.addLabel('R', row = 0, column = 0)
        self.addLabel('G', row = 1, column = 0)
        self.addLabel('B', row = 2, column = 0)
        self.addLabel("Color", row = 3, column = 0)
        self.r = self.addIntegerField(value = 0, row = 0, column = 1, sticky = "NSEW")
        self.g = self.addIntegerField(value = 0, row = 1, column = 1, sticky = "NSEW")
        self.b = self.addIntegerField(value = 0, row = 2, column = 1, sticky = "NSEW")
        self.hex = self.addTextField(text = "#000000", row = 3, column = 1, width = 10)
        
        #Canvas with initial black background
        self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")
        
        #Command button
        self.addButton(text = "Choose Color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)
        
    #Event handling method
    def chooseColor(self):
        #Pops up a color chooser and outputs the results
        colorTuple = tkinter.colorchooser.askcolor()
        if not colorTuple[0]:
            return
        ((r, g, b), hexString) = colorTuple
        self.r.setNumber(int(r))
        self.r.setNumber(int(g))
        self.r.setNumber(int(b))
        self.hex.setText(hexString)
        self.canvas["background"] = hexString
        
#Global defintion of the main function
def main():
    ColorPicker().mainloop()

#Global call to the main function
main()
