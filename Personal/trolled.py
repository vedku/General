import webbrowser
from tkinter import *
from tkinter import font

#tkinter setup
root = Tk()
root.title("DO NOT CLICK THE BUTTON")
root.geometry("1920x1080") 
def trolled(): 
    webbrowser.open("https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png")
'''
Text1 = Text(root, "hellO")
Text1.grid(row=0,column=2)
'''

myFont = font.Font(family='Arial', size=15, weight='bold')
## button declaration ##
#mon 
ButtonPure = Button(root, text="DO NOT CLICK THIS BUTTON", fg="#000000", bg="#FF0000", command=trolled, height=3, width=30) 
ButtonPure.grid(row=200,column=10,padx=5,pady=1)
root.mainloop()
