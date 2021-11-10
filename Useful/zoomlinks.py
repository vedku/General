#this is a modified version of Sonny's zoom organiser. Thanks Sonny for the help!
import webbrowser
from tkinter import * 
from tkinter import font

#tkinter setup
root = Tk()
root.title("Zoom Links GUI")
root.geometry("750x500")

## defining functions for zoom links ## 
#mon
def biology():
    webbrowser.open('https://gardenschool.zoom.us/j/95437832068?pwd=K1Z0SjQyWDh6L0lnNFZDV0RsN0ZUUT09') #insert zoom link here
def history():
    webbrowser.open('https://gardenschool.zoom.us/j/95575655186?pwd=RS92UDZ4RTRIS0xxd0g5a0l0L0dJZz09') #insert zoom link here
def english():
    webbrowser.open('https://gardenschool.zoom.us/j/96823418337?pwd=bWFBd0Y5NGRlVUNYTm5STGRhSDhDQT09') #insert zoom link here
def physics():
    webbrowser.open('https://gardenschool.zoom.us/j/94350319339?pwd=cmlURmhmL0cramlKbWpGVTNTalpqZz09') #insert zoom link here

#tuesday
def english():
    webbrowser.open('https://gardenschool.zoom.us/j/96823418337?pwd=bWFBd0Y5NGRlVUNYTm5STGRhSDhDQT09') #insert zoom link here
def history():
    webbrowser.open('https://gardenschool.zoom.us/j/95575655186?pwd=RS92UDZ4RTRIS0xxd0g5a0l0L0dJZz09') #insert zoom link here
def cs():
    webbrowser.open('https://gardenschool.zoom.us/j/92092880370?pwd=b1RlNUFpR3k5ejZZbyt5ci90ZGFKdz09') #insert zoom link here
def math():
    webbrowser.open('https://gardenschool.zoom.us/j/99638429784?pwd=UHRsdXFJZThhMVRwUnNwUXV2K0d1Zz09') #insert zoom link here

#wednesday
def chemistry():
    webbrowser.open('https://gardenschool.zoom.us/j/7962610360') #insert zoom link here
def physics():
    webbrowser.open('https://gardenschool.zoom.us/j/94350319339?pwd=cmlURmhmL0cramlKbWpGVTNTalpqZz09') #insert zoom link here
def english():
    webbrowser.open('https://gardenschool.zoom.us/j/96823418337?pwd=bWFBd0Y5NGRlVUNYTm5STGRhSDhDQT09') #insert zoom link here
def math():
    webbrowser.open('https://gardenschool.zoom.us/j/99638429784?pwd=UHRsdXFJZThhMVRwUnNwUXV2K0d1Zz09') #insert zoom link here

#thursday
def chemistry():
    webbrowser.open('https://gardenschool.zoom.us/j/7962610360') #insert zoom link here
def math():
    webbrowser.open('https://gardenschool.zoom.us/j/99638429784?pwd=UHRsdXFJZThhMVRwUnNwUXV2K0d1Zz09') #insert zoom link here
def cs():
    webbrowser.open('https://gardenschool.zoom.us/j/92092880370?pwd=b1RlNUFpR3k5ejZZbyt5ci90ZGFKdz09') #insert zoom link here
def economics():
    webbrowser.open('https://gardenschool.zoom.us/j/96347923163?pwd=SHdvbC9hQjUybDRCTHVEZk5mRmc0UT09') #insert zoom link here

#friday
def pe():
    webbrowser.open('https://gardenschool.zoom.us/j/5013154009') #insert zoom link here
def gap():
    webbrowser.open('https://gardenschool.zoom.us/j/3343226053') #insert zoom link here
def economics():
    webbrowser.open('https://gardenschool.zoom.us/j/96347923163?pwd=SHdvbC9hQjUybDRCTHVEZk5mRmc0UT09') #insert zoom link here
def biology():
    webbrowser.open('https://gardenschool.zoom.us/j/95437832068?pwd=K1Z0SjQyWDh6L0lnNFZDV0RsN0ZUUT09') #insert zoom link here



## text declaration ##
'''
Text1 = Text(root, "hellO")
Text1.grid(row=0,column=2)
'''

myFont = font.Font(family='Arial', size=15, weight='bold')
## button declaration ##
#mon 
ButtonTextPure = Button(root, text="Monday", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=0,padx=5)
ButtonPure = Button(root, text="Biology", fg="#000000", bg="#00ffff", command=biology, height=2, width=15) 
ButtonPure.grid(row=1,column=0,padx=5,pady=1)
ButtonPure = Button(root, text="History", fg="#000000", bg="#00ffff", command=history, height=2, width=15) 
ButtonPure.grid(row=2,column=0,padx=5,pady=1)
ButtonPure = Button(root, text="English", fg="#000000", bg="#00ffff", command=english, height=2, width=15) 
ButtonPure.grid(row=3,column=0,padx=5,pady=1)
ButtonPure = Button(root, text="Physics", fg="#000000", bg="#00ffff", command=physics, height=2, width=15) 
ButtonPure.grid(row=4,column=0,padx=5,pady=1)

#tue
ButtonTextPure = Button(root, text="Tuesday", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=1,padx=5)
ButtonPure = Button(root, text="English", fg="#000000", bg="#00ffff", command=english, height=2, width=15) 
ButtonPure.grid(row=1,column=1,padx=5,pady=1)
ButtonPure = Button(root, text="History", fg="#000000", bg="#00ffff", command=history, height=2, width=15) 
ButtonPure.grid(row=2,column=1,padx=5,pady=1)
ButtonPure = Button(root, text="CS", fg="#000000", bg="#00ffff", command=cs, height=2, width=15) 
ButtonPure.grid(row=3,column=1,padx=5,pady=1)
ButtonPure = Button(root, text="Math", fg="#000000", bg="#00ffff", command=math, height=2, width=15) 
ButtonPure.grid(row=4,column=1,padx=5,pady=1)

#wed
ButtonTextPure = Button(root, text="Wednesday", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=2,padx=5)
ButtonPure = Button(root, text="Chemistry", fg="#000000", bg="#00ffff", command=chemistry, height=2, width=15) 
ButtonPure.grid(row=1,column=2,padx=5,pady=1)
ButtonPure = Button(root, text="Physics", fg="#000000", bg="#00ffff", command=physics, height=2, width=15) 
ButtonPure.grid(row=2,column=2,padx=5,pady=1)
ButtonPure = Button(root, text="English", fg="#000000", bg="#00ffff", command=english, height=2, width=15) 
ButtonPure.grid(row=3,column=2,padx=5,pady=1)
ButtonPure = Button(root, text="Math", fg="#000000", bg="#00ffff", command=math, height=2, width=15) 
ButtonPure.grid(row=4,column=2,padx=5,pady=1)

#thu
ButtonTextPure = Button(root, text="Thursday", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=3,padx=5)
ButtonPure = Button(root, text="Chemistry", fg="#000000", bg="#00ffff", command=chemistry, height=2, width=15) 
ButtonPure.grid(row=1,column=3,padx=5,pady=1)
ButtonPure = Button(root, text="Math", fg="#000000", bg="#00ffff", command=math, height=2, width=15) 
ButtonPure.grid(row=2,column=3,padx=5,pady=1)
ButtonPure = Button(root, text="CS", fg="#000000", bg="#00ffff", command=cs, height=2, width=15) 
ButtonPure.grid(row=3,column=3,padx=5,pady=1)
ButtonPure = Button(root, text="Econs", fg="#000000", bg="#00ffff", command=economics, height=2, width=15) 
ButtonPure.grid(row=4,column=3,padx=5,pady=1)


#fri
ButtonTextPure = Button(root, text="Friday", state=DISABLED, font=myFont, fg="black", width=9)
ButtonTextPure.grid(row=0,column=4,padx=5)
ButtonPure = Button(root, text="PE", fg="#000000", bg="#00ffff", command=pe, height=2, width=15) 
ButtonPure.grid(row=1,column=4,padx=5,pady=1)
ButtonPure = Button(root, text="GAP", fg="#000000", bg="#00ffff", command=gap, height=2, width=15) 
ButtonPure.grid(row=2,column=4,padx=5,pady=1)
ButtonPure = Button(root, text="Econs", fg="#000000", bg="#00ffff", command=economics, height=2, width=15) 
ButtonPure.grid(row=3,column=4,padx=5,pady=1)
ButtonPure = Button(root, text="Biology", fg="#000000", bg="#00ffff", command=biology, height=2, width=15) 
ButtonPure.grid(row=4,column=4,padx=5,pady=1)
root.mainloop()
